# Agents and Workflows

Strategies for handling tasks that can't be completed by Claude in a single request.

---

## Workflows vs Agents

| | Workflow | Agent |
|--|---------|-------|
| **Control** | Predetermined steps | Claude decides the steps |
| **Flexibility** | Low — fixed path | High — dynamic path |
| **Predictability** | High | Lower |
| **Best for** | Structured, repeatable tasks | Open-ended, exploratory tasks |

---

## Workflows

A series of Claude calls arranged to solve a problem through a **fixed, predetermined sequence of steps**.

### Chaining Workflow

Each step's output becomes the next step's input. Used when a task has a clear linear order.

```
Input → [Step 1: Draft] → [Step 2: Review] → [Step 3: Format] → Output
```

**When to use:** Multi-stage tasks where each stage depends on the previous one (e.g. research → summarize → translate).

---

### Routing Workflow

A classifier step decides which downstream path to take. Used when different inputs require different handling.

```
Input → [Router] ──► [Path A: Technical support]
                 └──► [Path B: Billing support]
                 └──► [Path C: General enquiry]
```

**When to use:** When input type varies and each type needs a specialized handler.

---

### Parallelization Workflow

Multiple Claude calls run **simultaneously**, then results are aggregated. Two variants:

- **Sectioning** — Split a large task into independent chunks, run in parallel
- **Voting** — Run the same task multiple times, aggregate for consistency/confidence

```
         ┌──► [Worker A] ──┐
Input ───┼──► [Worker B] ──┼──► [Aggregator] → Output
         └──► [Worker C] ──┘
```

**When to use:** Large tasks with independent sub-tasks, or when confidence/accuracy matters.

---

## Agents

Claude is given a **goal** and a **set of tools** and determines its own path to completion. The loop continues until the task is done or a stopping condition is met.

```
Goal + Tools → [Claude] → tool_use? → Execute Tool → [Claude] → ... → Final Answer
```

### Agents & Tools

Tools give agents the ability to take actions in the world:

- **Read tools** — Fetch data (e.g. search, read file, query DB)
- **Write tools** — Modify state (e.g. write file, send message, call API)
- **Execution tools** — Run code or commands

Claude selects which tool to call, with what arguments, based on the current state of the task.

---

### Environment Inspection

Before acting, a well-designed agent inspects its environment to understand:

- What tools are available
- What the current state is (files, memory, previous results)
- What constraints apply

This allows the agent to plan appropriately rather than act blindly.

---

## Choosing the Right Strategy

| Scenario | Use |
|---------|-----|
| Fixed, predictable steps | **Chaining workflow** |
| Input varies, handling differs | **Routing workflow** |
| Independent sub-tasks | **Parallelization workflow** |
| Open-ended goal, flexible path | **Agent** |
