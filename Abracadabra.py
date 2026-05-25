'''
Abracadabra - Magic Card Trick (tkinter GUI)
'''

import tkinter as tk
from tkinter import font as tkfont
from random import shuffle

CARD_NUM = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
            7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}
SUITS = {"Spades": "♠", "Clubs": "♣", "Diamonds": "♦", "Hearts": "♥"}
RED_SUITS = {"♦", "♥"}

BG = "#1a1a2e"
CARD_BG = "#f5f0e8"
CARD_BORDER = "#c9b99a"
ACCENT = "#e94560"
TEXT_LIGHT = "#eaeaea"
BTN_BG = "#16213e"
BTN_HOVER = "#0f3460"
HIGHLIGHT = "#f5a623"


def full_deck():
    deck = []
    for suit_sym in SUITS.values():
        for num in CARD_NUM.values():
            deck.append((num, suit_sym))
    return deck


def random_cards(n):
    deck = full_deck()
    shuffle(deck)
    return deck[:n]


def sort_columns(deck, chosen_col):
    col1, col2, col3 = [], [], []
    for i, card in enumerate(deck):
        if i % 3 == 0:
            col1.append(card)
        elif i % 3 == 1:
            col2.append(card)
        else:
            col3.append(card)
    # Place the chosen column in the middle
    if chosen_col == 1:
        return col2 + col1 + col3
    elif chosen_col == 2:
        return col1 + col2 + col3
    else:
        return col1 + col3 + col2


class MagicTrickApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Abracadabra ✨")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.card_font = tkfont.Font(family="Courier New", size=11, weight="bold")
        self.title_font = tkfont.Font(family="Georgia", size=18, weight="bold")
        self.msg_font = tkfont.Font(family="Georgia", size=12, slant="italic")
        self.btn_font = tkfont.Font(family="Georgia", size=13, weight="bold")

        self.deck = []
        self.round_num = 0
        self.card_labels = []

        self._build_ui()
        self._new_game()

    def _build_ui(self):
        # Title
        tk.Label(self, text="✨  Abracadabra  ✨", font=self.title_font,
                 bg=BG, fg=ACCENT).pack(pady=(18, 4))

        # Message area
        self.msg_var = tk.StringVar()
        tk.Label(self, textvariable=self.msg_var, font=self.msg_font,
                 bg=BG, fg=TEXT_LIGHT, wraplength=480, justify="center").pack(pady=(0, 10))

        # Card grid frame
        self.grid_frame = tk.Frame(self, bg=BG)
        self.grid_frame.pack(padx=20)

        # Column headers
        for col_idx, label in enumerate(["Column 1", "Column 2", "Column 3"]):
            tk.Label(self.grid_frame, text=label, font=self.btn_font,
                     bg=BG, fg=HIGHLIGHT, width=8).grid(row=0, column=col_idx, padx=8, pady=(0, 4))

        # Card label grid (7 rows x 3 cols)
        self.card_labels = []
        for row in range(7):
            row_labels = []
            for col in range(3):
                lbl = tk.Label(self.grid_frame, text="", font=self.card_font,
                               bg=CARD_BG, fg="#222", relief="raised", bd=2,
                               width=5, height=2, anchor="center")
                lbl.grid(row=row + 1, column=col, padx=8, pady=3)
                row_labels.append(lbl)
            self.card_labels.append(row_labels)

        # Column select buttons
        self.btn_frame = tk.Frame(self, bg=BG)
        self.btn_frame.pack(pady=14)

        self.col_buttons = []
        for i in range(1, 4):
            btn = tk.Button(self.btn_frame, text=f"Column {i}", font=self.btn_font,
                            bg=BTN_BG, fg=TEXT_LIGHT, activebackground=BTN_HOVER,
                            activeforeground=TEXT_LIGHT, relief="flat", bd=0,
                            padx=18, pady=8, cursor="hand2",
                            command=lambda c=i: self._column_selected(c))
            btn.pack(side="left", padx=10)
            btn.bind("<Enter>", lambda *_, b=btn: b.configure(bg=BTN_HOVER))
            btn.bind("<Leave>", lambda *_, b=btn: b.configure(bg=BTN_BG))
            self.col_buttons.append(btn)

        # Reveal / play again area
        self.reveal_frame = tk.Frame(self, bg=BG)
        self.reveal_frame.pack(pady=6)

        self.reveal_var = tk.StringVar()
        self.reveal_label = tk.Label(self.reveal_frame, textvariable=self.reveal_var,
                                     font=tkfont.Font(family="Georgia", size=20, weight="bold"),
                                     bg=BG, fg=ACCENT)
        self.reveal_label.pack()

        self.again_btn = tk.Button(self.reveal_frame, text="Play Again", font=self.btn_font,
                                   bg=ACCENT, fg="white", activebackground="#c73652",
                                   relief="flat", padx=20, pady=8, cursor="hand2",
                                   command=self._new_game)
        self.again_btn.pack(pady=6)
        self.again_btn.pack_forget()

    def _new_game(self):
        self.deck = random_cards(21)
        self.round_num = 0
        self.picked_card = None
        self.reveal_var.set("")
        self.again_btn.pack_forget()
        self._set_buttons_state("normal")
        self.msg_var.set("Pick a card... Shhh, don't tell me what it is!\nThen click the column it's in.")
        self._display_cards(self.deck)

    def _display_cards(self, deck, highlight_col=None):
        for row in range(7):
            for col in range(3):
                idx = row * 3 + col
                card = deck[idx]
                num, suit = card
                text = f"{num}{suit}"
                color = ACCENT if suit in RED_SUITS else "#1a1a2e"
                bg = HIGHLIGHT if highlight_col == col + 1 else CARD_BG
                self.card_labels[row][col].configure(text=text, fg=color, bg=bg)

    def _set_buttons_state(self, state):
        for btn in self.col_buttons:
            btn.configure(state=state)

    def _column_selected(self, col):
        self._set_buttons_state("disabled")
        self._display_cards(self.deck, highlight_col=col)
        self.round_num += 1

        self.deck = sort_columns(self.deck, col)

        if self.round_num < 3:
            prompts = [
                "Good... now I'm reshuffling.\nFind your card again and click its column.",
                "Almost there... one more time.\nPoint to the column holding your card."
            ]
            self.after(700, lambda: self._next_round(prompts[self.round_num - 1]))
        else:
            self.picked_card = self.deck[10]
            self.after(700, self._reveal_sequence)

    def _next_round(self, prompt):
        self._display_cards(self.deck)
        self.msg_var.set(prompt)
        self._set_buttons_state("normal")

    def _reveal_sequence(self):
        self._display_cards(self.deck)
        self.msg_var.set("Hmmmm... I'm reading your mind...")
        self.after(1200, lambda: self.msg_var.set("The cards are speaking to me..."))
        self.after(2400, lambda: self.msg_var.set("Yes... YES... I see it now!"))
        self.after(3600, self._show_reveal)

    def _show_reveal(self):
        num, suit = self.picked_card
        self.msg_var.set("Your card was...")
        self.reveal_var.set(f"{num} {suit}")
        self.again_btn.pack(pady=6)


if __name__ == "__main__":
    app = MagicTrickApp()
    app.mainloop()
