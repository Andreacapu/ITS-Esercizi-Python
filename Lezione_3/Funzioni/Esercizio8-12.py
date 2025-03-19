def panino(*ingredienti):
        print("\nIn arrivo un panino con i seguenti ingredienti: ")
        for ingrediente in ingredienti:
            print(f"- {ingredienti}")

panino("prosciutto", "formaggio")
panino("tonno", "gamberetti", "salsa rosa")
panino("uova", "tonno", "pomodori")

