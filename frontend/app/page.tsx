

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-100 p-4">
      <main className="flex w-full max-w-4xl flex-col items-center gap-8 rounded-xl bg-white p-8 shadow-lg">
        <h1 className="text-4xl font-bold text-gray-900">
          🛡️ Secure Document Vault
        </h1>

        <div className="grid w-full grid-cols-1 gap-4 md:grid-cols-2">
          <div className="rounded-lg border border-gray-200 p-6">
            <h2 className="mb-2 text-xl font-semibold text-gray-800">Backend Status</h2>
            <p className="text-gray-600">Checking...</p>
          </div>

          <div className="rounded-lg border border-gray-200 p-6">
            <h2 className="mb-2 text-xl font-semibold text-gray-800">Mayan EDMS</h2>
            <p className="text-gray-600">
              <a href="http://localhost:8000" target="_blank" className="text-blue-600 hover:underline">
                Open Mayan EDMS &rarr;
              </a>
            </p>
          </div>
        </div>

        <div className="mt-8 text-sm text-gray-500">
          Nuit de l'Info 2024 Challenge
        </div>
      </main>
    </div>
  );
}
