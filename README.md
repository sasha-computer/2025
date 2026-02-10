# 2025

Monorepo for my 2025 projects.

## ⭐ Highlights

### [browser-verifier](./browser-verifier)
A full-stack in-browser ZK proof verifier. Uses R0VM for ZK proving, compiled to WebAssembly via `wasm-pack`, served through a Next.js app. Verifies a proof of the 1,000,000th Fibonacci number directly in the browser — in a fraction of the time it takes to calculate it directly. Includes a [video walkthrough](https://www.youtube.com/watch?v=aTCPCf8ff-c).

### [cubes](./cubes)
An interactive personal site built with SvelteKit and Three.js. Navigate a rolling cube across an 8×8 chess-style grid using arrow keys — land on highlighted tiles to reveal content like blog posts and reading lists. Smooth roll animations with pivot-point physics and eased quaternion interpolation.

---

## Other Projects

| Project | Description |
|---------|-------------|
| [nn](./nn) | Code for the Zero to Hero Neural Net series from Andrej Karpathy |
| [vocs-search-fix](./vocs) | Fix for [wevm/vocs](https://github.com/wevm/vocs) search indexing ([issue #276](https://github.com/wevm/vocs/issues/276)) — MDX files with local imports/components were silently failing to index for search. Patched `processMdx` to strip imports and component tags before indexing. Published as a [release](https://github.com/sasha-computer/vocs/releases/tag/v1.0.13-search-fix-release) with 270+ downloads. |
| [day-one-aoc-2025](./day-one-aoc-2025) | Day 1 of Advent of Code 2025 — handwritten Python |
