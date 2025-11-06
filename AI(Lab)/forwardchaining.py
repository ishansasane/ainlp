# Simple Troubleshooting Expert System

# Knowledge base (rules)
rules = [
    ([("problem", "power_light_off")], ("solution", "check_power_supply")),
    ([("problem", "computer_not_starting"), ("solution", "power_supply_ok")], ("solution", "check_RAM")),
    ([("problem", "blank_display"), ("solution", "power_supply_ok")], ("solution", "check_monitor_cable")),
    ([("problem", "computer_not_starting"), ("problem", "blank_display")], ("solution", "check_graphics_card")),
    ([("problem", "strange_beep")], ("solution", "check_motherboard")),
    ([("problem", "computer_not_starting"), ("problem", "strange_beep")], ("solution", "check_hard_disk")),
    ([("problem", "computer_not_starting"), ("solution", "RAM_ok")], ("solution", "check_operating_system")),
]

# Forward chaining function
def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for premises, conclusion in rules:
            if all(p in inferred for p in premises):
                if conclusion not in inferred:
                    inferred.add(conclusion)
                    changed = True
    return inferred

# Main program
if __name__ == "__main__":
    print("=== Troubleshooting Expert System ===")
    print("Enter observed problems (symptoms).")
    print("Available problems:")
    print("- computer_not_starting\n- power_light_off\n- blank_display\n- strange_beep")
    print("Type 'done' when finished.\n")

    facts = []

    while True:
        symptom = input("Enter a problem (or 'done'): ").strip().lower()
        if symptom == "done":
            break
        elif symptom in ["computer_not_starting", "power_light_off", "blank_display", "strange_beep"]:
            facts.append(("problem", symptom))
        else:
            print("Unknown problem. Please choose from the list.\n")

    inferred_facts = forward_chaining(facts, rules)

    print("\nSuggested Actions / Solutions:")
    solutions = [f[1] for f in inferred_facts if f[0] == "solution"]

    if solutions:
        for s in solutions:
            print("-", s)
    else:
        print("No solution found. Please provide more symptoms.")
