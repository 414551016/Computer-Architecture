from build_prompts import E, prefix
import json

plain={
'p1_critique':'Critique your preceding sort_tasks_by_priority implementation against these requirements: high/medium/low priority order; ascending dates within each tier; None last within its tier, including when a dated task has date.max; stable ties; a new list with no input mutation; empty input. For each criterion give PASS or FAIL with a specific reason or counterexample. Distinguish inspection from tests actually run. Do not invent defects if the code is correct. Then identify any unnecessary complexity under the valid-input assumption. Do not revise the code yet.',
'p1_revision':'Revise the implementation based on that critique. Keep every original requirement, including None sorting after an actual date.max and stable equal keys. Under the stated valid-input assumption, remove unnecessary fallbacks and avoid an unnecessary date import while keeping the code readable. Return only the complete function in one Python code block.',
}
rewrites={
'p2_rewrite_1':"Implement add_subtask(tasks, parent_title, subtask_title). Follow these project conventions explicitly: define TaskError as a subclass of Exception in the same file; if the parent is absent raise TaskError, never return False or None as a failure signal. Match titles ignoring case and leading/trailing spaces. Append a new subtask dictionary to the parent's subtasks list, creating that list if absent. The new dictionary must have exactly title=subtask_title, due_date=None, priority equal to the parent's priority, and completed=False. Return the same updated tasks list object. Keep other tasks unchanged. Give the function a Google-style docstring with Args: and Returns: (and document the exception). Assume valid task dictionaries and a list-valued subtasks field when present; on duplicate matching titles use the first match. Return only TaskError and the function in one Python code block.",
'p2_rewrite_3':'Implement get_urgent_tasks(tasks, today) with this explicit specification. Exclude all completed tasks. Include an incomplete task if its priority is high OR it has a due date no later than today + timedelta(days=3); this includes all overdue dates, today, and exactly three days ahead. A non-high task due four days ahead is excluded. A high-priority task is included even when due later or undated. Return a new list sorted by earliest due date first across all priorities, placing undated high-priority tasks last, including after an actual date.max. Preserve input order for equal dates. Do not modify the input list or dictionaries. Return [] for empty input. Assume valid task dictionaries with date or None due dates. Include a Google-style docstring with Args: and Returns:. Return only the necessary standard-library imports and function in one Python code block.',
}
helper='''def due_label(due, today):
    """Return no due date, due today, due in N day(s), or overdue by N day(s)."""
    if due is None:
        return "no due date"
    delta = (due - today).days
    if delta == 0:
        return "due today"
    if delta > 0:
        return f"due in {delta} day" + ("" if delta == 1 else "s")
    return f"overdue by {-delta} day" + ("" if delta == -1 else "s")
'''
rewrites['p2_rewrite_2']='The existing utils.py provides the following implementation (docstring abbreviated here; logic unchanged):\n```python\n'+helper+'```\n\nImplement format_task_line(task, today). Import and call utils.due_label(task["due_date"], today) for every task, including None dates; do not invent another helper or duplicate its logic. Return one line in the format TITLE [PRIORITY] - DUE_LABEL, preserving the title and lowercase priority exactly and the helper result verbatim. Assume valid task dictionaries with single-line titles. Do not modify the task or utils.py. Include a Google-style docstring with Args: and Returns:. Return only the necessary import and function in one Python code block.'
for key,value in plain.items():
    (E/f'{key}_prompt.txt').write_text(value,encoding='utf-8')
for key,value in rewrites.items():
    (E/f'{key}_prompt.txt').write_text(prefix+value,encoding='utf-8')
sources=json.loads((E/'conversation_sources.json').read_text())
sources.update({
'p1_step':'https://gemini.google.com/app/9ec382ff4007f8a3',
'p1_zero':'https://gemini.google.com/app/6a0f78235b8723ec',
'p1_critique':'https://gemini.google.com/app/6a0f78235b8723ec',
'p1_revision':'https://gemini.google.com/app/6a0f78235b8723ec',
'p1_few':'https://gemini.google.com/app/f153f6d5054ce55b',
'p2_rewrite_1':'https://gemini.google.com/app/9a14ca980f938399',
'p2_rewrite_2':'https://gemini.google.com/app/ba5c0929c82816c2',
'p2_rewrite_3':'https://gemini.google.com/app/728afbcd4ebe491f',
})
(E/'conversation_sources.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
print('All submitted prompts and source conversation URLs saved.')
