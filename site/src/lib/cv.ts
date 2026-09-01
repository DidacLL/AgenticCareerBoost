import manifest from "../../../agents/cv/artifacts.json";

const artifact = manifest.artifacts.find(
  (item) => item.kind === "cv" && item.publish
);

if (!artifact) {
  throw new Error("Public CV artifact is missing.");
}

export const publicCvPath = artifact.sitePdf.replace(/^site\/assets\//, "");
