const indexable = import.meta.env.SITE_INDEXABLE === "true";
const origin = import.meta.env.SITE_ORIGIN || "https://example.invalid";

export function GET() {
  const body = indexable
    ? `User-agent: *\nAllow: /\nSitemap: ${new URL("/sitemap-index.xml", origin).toString()}\n`
    : "User-agent: *\nDisallow: /\n";

  return new Response(body, {
    headers: {
      "content-type": "text/plain; charset=utf-8"
    }
  });
}
