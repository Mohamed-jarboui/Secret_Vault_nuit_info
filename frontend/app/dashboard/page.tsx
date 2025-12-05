'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

interface Document {
    id: number;
    label: string;
    summary?: string;
}

export default function DashboardPage() {
    const [file, setFile] = useState<File | null>(null);
    const [searchQuery, setSearchQuery] = useState('');
    const [documents, setDocuments] = useState<Document[]>([]);
    const [uploadStatus, setUploadStatus] = useState('');
    const router = useRouter();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            router.push('/login');
        }
    }, [router]);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files) {
            setFile(e.target.files[0]);
        }
    };

    const handleUpload = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!file) return;

        setUploadStatus('Uploading & Analyzing...');
        const formData = new FormData();
        formData.append('file', file);

        try {
            const token = localStorage.getItem('token');
            const res = await fetch('http://localhost:5000/api/v1/documents/upload', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
                body: formData,
            });

            if (!res.ok) {
                const errData = await res.json();
                throw new Error(errData.detail || 'Upload failed');
            }

            const data = await res.json();
            setUploadStatus(`Success! AI Summary: ${data.ai_summary}`);
            // Refresh list (mock)
            setDocuments([...documents, { id: Date.now(), label: file.name, summary: data.ai_summary }]);
        } catch (err: any) {
            setUploadStatus(`Error: ${err.message}`);
        }
    };

    const handleSearch = async () => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch(`http://localhost:5000/api/v1/documents/search?q=${searchQuery}`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });
            const data = await res.json();
            setDocuments(data);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div className="min-h-screen bg-zinc-950 text-white">
            <nav className="border-b border-zinc-800 bg-zinc-900 p-4">
                <div className="container mx-auto flex items-center justify-between">
                    <h1 className="text-xl font-bold">🛡️ Vault Dashboard</h1>
                    <button
                        onClick={() => {
                            localStorage.removeItem('token');
                            router.push('/login');
                        }}
                        className="text-sm text-zinc-400 hover:text-white"
                    >
                        Sign out
                    </button>
                </div>
            </nav>

            <main className="container mx-auto p-8">
                <div className="grid gap-8 md:grid-cols-2">
                    {/* Upload Section */}
                    <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-6">
                        <h2 className="mb-4 text-xl font-semibold">Upload Document</h2>
                        <form onSubmit={handleUpload} className="space-y-4">
                            <div className="flex items-center justify-center w-full">
                                <label className="flex flex-col items-center justify-center w-full h-32 border-2 border-zinc-700 border-dashed rounded-lg cursor-pointer bg-zinc-800 hover:bg-zinc-700">
                                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                        <p className="mb-2 text-sm text-zinc-400">
                                            <span className="font-semibold">Click to upload</span> or drag and drop
                                        </p>
                                    </div>
                                    <input type="file" className="hidden" onChange={handleFileChange} />
                                </label>
                            </div>
                            {file && <p className="text-sm text-zinc-400">Selected: {file.name}</p>}
                            <button
                                type="submit"
                                className="w-full rounded-md bg-indigo-600 py-2 px-4 font-medium hover:bg-indigo-700"
                            >
                                Upload & Analyze
                            </button>
                        </form>
                        {uploadStatus && (
                            <div className="mt-4 rounded bg-zinc-800 p-3 text-sm text-zinc-300">
                                {uploadStatus}
                            </div>
                        )}
                    </div>

                    {/* Search Section */}
                    <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-6">
                        <h2 className="mb-4 text-xl font-semibold">Search Vault</h2>
                        <div className="flex gap-2">
                            <input
                                type="text"
                                placeholder="Search documents..."
                                className="flex-1 rounded-md border-0 bg-zinc-800 py-2 px-3 text-white focus:ring-2 focus:ring-indigo-500"
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                            />
                            <button
                                onClick={handleSearch}
                                className="rounded-md bg-zinc-700 py-2 px-4 hover:bg-zinc-600"
                            >
                                Search
                            </button>
                        </div>

                        <div className="mt-6 space-y-4">
                            {documents.map((doc) => (
                                <div key={doc.id} className="rounded-lg bg-zinc-800 p-4">
                                    <h3 className="font-medium text-indigo-400">{doc.label}</h3>
                                    {doc.summary && (
                                        <p className="mt-2 text-sm text-zinc-400">{doc.summary}</p>
                                    )}
                                </div>
                            ))}
                            {documents.length === 0 && (
                                <p className="text-center text-sm text-zinc-500">No documents found.</p>
                            )}
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}
