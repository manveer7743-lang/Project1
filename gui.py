import importlib.util
from pathlib import Path
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


_algorithm_path = Path(__file__).with_name("6174.py")
_algorithm_spec = importlib.util.spec_from_file_location(
    "kaprekar_algorithm", _algorithm_path
)
if _algorithm_spec is None or _algorithm_spec.loader is None:
    raise ImportError(f"Unable to load Kaprekar functions from {_algorithm_path}")
_algorithm = importlib.util.module_from_spec(_algorithm_spec)
_algorithm_spec.loader.exec_module(_algorithm)
validate = _algorithm.validate
kaprekar = _algorithm.kaprekar


def main():
    root = tk.Tk()
    root.title("Kaprekar's Routine")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(3, weight=1)

    tk.Label(root, text="Enter a 3 or 4 digit number:").grid(
        row=0, column=0, padx=10, pady=(10, 0), sticky="w"
    )

    number_var = tk.StringVar()
    number_entry = tk.Entry(root, textvariable=number_var)
    number_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    error_label = tk.Label(root, text="", fg="red", anchor="w")
    error_label.grid(row=2, column=0, padx=10, sticky="ew")

    steps_area = ScrolledText(root, height=12, width=40, state="disabled")
    steps_area.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

    iteration_label = tk.Label(root, text="Iterations: ")
    iteration_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    def clear_output():
        error_label.config(text="")
        steps_area.config(state="normal")
        steps_area.delete("1.0", tk.END)
        steps_area.config(state="disabled")
        iteration_label.config(text="Iterations: ")

    def calculate(event=None):
        x = number_entry.get()
        error = validate(x)
        if error is not None:
            clear_output()
            error_label.config(text=error)
            return

        steps, iterations = kaprekar(x)
        error_label.config(text="")
        steps_area.config(state="normal")
        steps_area.delete("1.0", tk.END)
        steps_area.insert(tk.END, "\n".join(steps))
        steps_area.tag_configure(
            "final_step", foreground="green", font=("TkDefaultFont", 10, "bold")
        )
        steps_area.tag_add("final_step", f"{len(steps)}.0", f"{len(steps)}.end")
        steps_area.config(state="disabled")
        iteration_label.config(text=f"Iterations: {iterations}")

    button_frame = tk.Frame(root)
    button_frame.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="ew")
    button_frame.columnconfigure((0, 1), weight=1)

    def clear():
        number_var.set("")
        clear_output()

    calculate_button = tk.Button(button_frame, text="Calculate", command=calculate)
    calculate_button.grid(row=0, column=0, sticky="ew", padx=(0, 5))
    clear_button = tk.Button(button_frame, text="Clear", command=clear)
    clear_button.grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def update_calculate_state(*args):
        state = tk.NORMAL if number_var.get().strip() else tk.DISABLED
        calculate_button.config(state=state)

    number_var.trace_add("write", update_calculate_state)
    update_calculate_state()

    number_entry.bind("<Return>", calculate)
    number_entry.focus_set()
    root.mainloop()


if __name__ == "__main__":
    main()
