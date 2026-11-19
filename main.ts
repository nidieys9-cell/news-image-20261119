// news-image-20261119 — entry point, rewritten by hand in this session.
// Job is deliberately tiny: ship the pre-rendered entry.png as-is.
// The picture itself is produced ahead of time (see draw.py); at run
// time we only have to place a byte-identical copy into whatever
// output folder the platform points MAKEFUN_OUTPUT_DIR at.

import { createReadStream, createWriteStream, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { pipeline } from "node:stream/promises";

// Folder this file lives in — entry.png sits right next to it.
const here = dirname(fileURLToPath(import.meta.url));
const sourceFile = join(here, "entry.png");

// Fall back to /output when the platform does not tell us otherwise.
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const targetFile = join(targetDir, "entry.png");

mkdirSync(targetDir, { recursive: true });

// Stream the copy instead of loading the whole PNG into memory.
await pipeline(createReadStream(sourceFile), createWriteStream(targetFile));

const bytesCopied = statSync(targetFile).size;
const bytesExpected = statSync(sourceFile).size;
if (bytesCopied !== bytesExpected) {
  throw new Error(`copy looks truncated: got ${bytesCopied}, want ${bytesExpected}`);
}
console.log(`entry.png copied: ${bytesCopied} bytes -> ${targetFile}`);
