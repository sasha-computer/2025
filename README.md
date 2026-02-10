# 2025

Monorepo for my 2025 projects.

## ⭐ browser-verifier

A full-stack in-browser ZK proof verifier. Compiles a [R0VM](https://dev.risczero.com/api/zkvm/quickstart) Rust verifier to WebAssembly via `wasm-pack` and serves it through a Next.js app. The demo calculates the 1,000,000th Fibonacci number — then verifies a ZK proof of that computation directly in the browser, in a fraction of the time it takes to calculate it from scratch. Includes a [video walkthrough](https://www.youtube.com/watch?v=aTCPCf8ff-c).

**Stack:** Rust · R0VM · wasm-pack · WebAssembly · Next.js

→ [browse code](./browser-verifier)

## ⭐ cubes

An interactive personal site concept built with SvelteKit and Three.js. You roll a coloured cube across an 8×8 chess-style grid using arrow keys — landing on highlighted tiles reveals content panels (blog posts, reading lists). Features smooth pivot-point roll animations with eased quaternion interpolation, per-face materials, and a responsive split-screen layout.

**Stack:** SvelteKit · Three.js · TypeScript

→ [browse code](./cubes)

## ⭐ vocs-search-fix

Fix for [wevm/vocs](https://github.com/wevm/vocs) search indexing ([upstream issue #276](https://github.com/wevm/vocs/issues/276)). MDX files with local imports and custom components were silently failing to get indexed for search — `processMdx` would error out on unresolvable imports at build time. The fix strips import/export statements and component tags from MDX before indexing, so all page content is searchable without breaking the build. Published as a [patched release](https://github.com/sasha-computer/vocs/releases/tag/v1.0.13-search-fix-release) (270+ downloads). The fork is kept alive at [sasha-computer/vocs](https://github.com/sasha-computer/vocs) for anyone pinned to it.

**Stack:** TypeScript · MDX · Vite

→ [browse code](./vocs)

## ⭐ nn

Working through Andrej Karpathy's [Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) neural net series from scratch. Built a custom autograd engine (`Node` class) with full backpropagation support — addition, multiplication, power, tanh activation — then used it to construct and train a multi-layer perceptron. Also experimented with [tinygrad](https://github.com/tinygrad/tinygrad) for GPU-accelerated tensor ops on Apple Metal.

**Stack:** Python · NumPy · Matplotlib · tinygrad

→ [browse code](./nn)

## ⭐ day-one-aoc-2025

Day 1 of [Advent of Code 2025](https://adventofcode.com/2025) — both parts, handwritten Python, no AI. A dial rotation puzzle: parse directional instructions, simulate modular arithmetic on a 0–99 dial, and count zero-crossings. Part 2 adds directional awareness to the crossing logic.

**Stack:** Python

→ [browse code](./day-one-aoc-2025)
