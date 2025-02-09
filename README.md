<!--
 * @Author: Zihui Cheng
 * @Date: 2024-12-16 09:37:02
 * @LastEditors: Zihui Cheng
 * @LastEditTime: 2025-02-09 17:02:55
 * @Description: 
-->
<p align="center">
<h1 align="center"> <img src="imgs/title.png" alt="SVG Image" width="40px" style="vertical-align: middle;"> CoMT: A Novel Benchmark for Chain of Multi-modal Thought on Large Vision-Language Models</h1>
</p>
<p align="center">
  	<a href="https://img.shields.io/badge/version-v0.0.1-blue">
      <img alt="version" src="https://img.shields.io/badge/version-v0.0.1-blue?color=FF8000?color=009922" />
    </a>
    <a >
       <img alt="PRs-Welcome" src="https://img.shields.io/badge/PRs-Welcome-blue" />
  	</a>
   	<a href="https://github.com/czhhzc/CoMT/stargazers">
       <img alt="stars" src="https://img.shields.io/github/stars/czhhzc/CoMT" />
  	</a>
  	<a href="https://github.com/czhhzc/CoMT/network/members">
       <img alt="FORK" src="https://img.shields.io/github/forks/czhhzc/CoMT?color=FF8000" />
  	</a>
    <a href="https://github.com/czhhzc/CoMT/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/czhhzc/CoMT?color=0088ff"/>
    </a>
    <br />
</p>

<p align="center">
  	<b>
    | [<a href="https://arxiv.org/abs/2412.12932">ArXiv</a>] | [<a href="https://huggingface.co/datasets/czh-up/comt">🤗HuggingFace</a>] |
    </b>
    <br />
</p>

🌟 Any contributions via PRs, issues, emails or other methods are greatly appreciated.

## 🔥News
- 🎖️ **Our work is accepted by AAAI 2025 !**
- 🔥 **We have release benchmark on \[[🤗HuggingFace](https://huggingface.co/datasets/czh-up/comt)\].**
- 🔥 **The paper is also available on \[[ArXiv](https://arxiv.org/abs/2412.12932)\].**

## 💡 Motivation
Large Vision-Language Models (LVLMs) have recently demonstrated amazing success in multi-modal tasks, including advancements in Multi-modal Chain-of-Thought (MCoT) reasoning. Despite these successes, current benchmarks still follow a traditional paradigm with multi-modal input and text-modal output, which leads to significant drawbacks such as missing visual operations and vague expressions. Motivated by this, we introduce a novel **Chain of Multi-modal Thought (CoMT)** benchmark to address these limitations. Different from the traditional MCoT benchmark, CoMT requires both multi-modal input and multi-modal reasoning output, aiming to mimic human-like reasoning that inherently integrates visual operation. Specifically, CoMT consists of four categories: (1) **Visual Creation**, (2) **Visual Deletion**, (3) **Visual Update**, and (4) **Visual Selection** to comprehensively explore complex visual operations and concise expression in real scenarios. We evaluate various LVLMs and strategies on CoMT, revealing some key insights into the capabilities and limitations of the current approaches. We hope that CoMT can inspire more research on introducing multi-modal generation into the reasoning process.

## 🎯 Installation

### Dataset Preparation
#### Load Dataset from Huggingface
```python 
import datasets
dataset = datasets.load_dataset("czh-up/comt")
```

The data follows the format below:
```json
{
  "id": "[ID]",
  "question": "[QUESTION]",
  "option": ["[OPTION1]", "[OPTION2]", ...],
  "image": ["IMAGE"],
  "rationale": "[RATIONALE]",
  "answer": "A/B/C/D",
  "type": "[TYPE]", // the task type, like add, delete, ...
  "annotations": "[ANNOTATIONS]" // grounding coordinates or tangram annotations, etc
}
```

## ✒️ Reference
If you find this project useful for your research, please consider citing the following paper:

```
@article{cheng2024comt,
  title={CoMT: A Novel Benchmark for Chain of Multi-modal Thought on Large Vision-Language Models},
  author={Cheng, Zihui and Chen, Qiguang and Zhang, Jin and Fei, Hao and Feng, Xiaocheng and Che, Wanxiang and Li, Min and Qin, Libo},
  journal={arXiv preprint arXiv:2412.12932},
  year={2024}
}
```

## 📲 Contact

Please create Github issues here or email [Zihui Cheng](mailto:upupczh@gmail.com) if you have any questions or suggestions. 
