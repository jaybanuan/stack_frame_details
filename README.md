# stack_frame_details

```
$ python3 stack_frame_details.py
[
    {
        "code_context": [
            "    for stack_frame in inspect.stack():\n"
        ],
        "count": {},
        "filename": "/home/jaybanuan/src/stack_frame_details/stack_frame_ditails.py",
        "frame": {
            "f_code": {
                "co_argcount": 0,
                "co_filename": "/home/jaybanuan/src/stack_frame_details/stack_frame_ditails.py",
                "co_firstlineno": 36,
                "co_flags": 67,
                "co_kwonlyargcount": 0,
                "co_lines": {},
                "co_name": "collect_stackframe_details",
                "co_nlocals": 2,
                "co_posonlyargcount": 0,
                "co_stacksize": 6
            },
            "f_lasti": 26,
            "f_lineno": 40,
            "f_trace": null,
            "f_trace_lines": true,
            "f_trace_opcodes": false
        },
        "function": "collect_stackframe_details",
        "index": 0,
        "lineno": 39
    },
    {
        "code_context": [
            "print(json.dumps(collect_stackframe_details(), indent=4))        \n"
        ],
        "count": {},
        "filename": "/home/jaybanuan/src/stack_frame_details/stack_frame_ditails.py",
        "frame": {
            "f_code": {
                "co_argcount": 0,
                "co_filename": "/home/jaybanuan/src/stack_frame_details/stack_frame_ditails.py",
                "co_firstlineno": 1,
                "co_flags": 64,
                "co_kwonlyargcount": 0,
                "co_lines": {},
                "co_name": "<module>",
                "co_nlocals": 0,
                "co_posonlyargcount": 0,
                "co_stacksize": 7
            },
            "f_lasti": 148,
            "f_lineno": 45,
            "f_trace": null,
            "f_trace_lines": true,
            "f_trace_opcodes": false
        },
        "function": "<module>",
        "index": 0,
        "lineno": 45
    }
]
```
