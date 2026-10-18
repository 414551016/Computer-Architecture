from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parent
E = ROOT / 'evidence'
M = ROOT / 'materials' / 'csic30216-fall26-assignment1'
module = (E / 'task_manager_from_assignment.py').read_text(encoding='utf-8')
assert ast.dump(ast.parse(module)) == ast.dump(ast.parse((M/'task_manager.py').read_text(encoding='utf-8')))
prefix = 'task_manager.py:\n```python\n' + module + '```\n\n'
prompts = {
 'p2_original_1': 'Write a function add_subtask(tasks, parent_title, subtask_title) that adds a subtask to an existing task.',
 'p2_original_2': 'Write a function format_task_line(task, today) that returns a one-line display string for a task, showing its title, priority and due date. Use our existing date-formatting helper in utils.py for the due date.',
 'p2_original_3': 'Write a function get_urgent_tasks(tasks, today) that returns the urgent tasks, most urgent first.',
 'p1_cot': 'Debug get_overdue_tasks. It crashes with TypeError when a task has due_date=None. Give a concise step-by-step execution trace explaining the cause before the corrected function. Preserve the meaning: return incomplete tasks with a date strictly before current_date, and do not modify the input. Return only the short explanation and corrected function.',
 'p1_step': 'Debug get_overdue_tasks for tasks whose due_date is None. First step back: briefly state the general principles for comparing optional dates and using short-circuit conditions. Then apply those principles to this function and provide the corrected function. Preserve incomplete tasks with dates strictly before current_date, exclude undated tasks, and do not modify the input. Keep the explanation concise.',
 'p1_zero': 'Implement sort_tasks_by_priority(tasks). Return a new list of the task dictionaries sorted by priority high, medium, low; within each priority, earlier due dates first and tasks with due_date=None last. Preserve input order for equal keys, do not modify the input list or dictionaries, and return [] for empty input. Assume valid task dictionaries as produced by add_task. Return only the function and any required standard-library imports in one Python code block.',
 'p1_few': 'Use the two provided docstrings of add_task and mark_complete as examples of the documentation style. Write a matching Google-style docstring for calculate_completion_rate, with a one-line summary, Args: and Returns:. Describe the actual return value and the empty-list behavior. Do not change the function logic. Return only calculate_completion_rate with its docstring in one Python code block.',
}
for key, value in prompts.items():
    (E/f'{key}_prompt.txt').write_text(prefix+value,encoding='utf-8')
sources={
 'p2_original_1':'https://gemini.google.com/app/1e2f9404c5488862',
 'p2_original_2':'https://gemini.google.com/app/900ce23410ba3228',
 'p2_original_3':'https://gemini.google.com/app/6c39def865e8b545',
 'p1_cot':'https://gemini.google.com/app/02ebbb9f6f4072b7',
}
(E/'conversation_sources.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
print('Saved exact prompt payloads; PDF/web module AST matches the instructor module.')
