#include <iostream>
#include <string>
#include <sstream>
#include <customtkinter.hpp>

void copyToClipboard(const std::string& text) {
    // Clipboard copy functionality using pyperclip
    // pyperclip.copy(text);
}

void resetFields(customtkinter::Textbox* inputField, customtkinter::Label* resultLabel) {
    inputField->delete(0, customtkinter::END);
    resultLabel->set_text("文字数: 0, 単語数: 0");
}

void countCharactersAndWords(customtkinter::Textbox* inputField, customtkinter::Label* resultLabel) {
    std::string text = inputField->get_text();
    std::istringstream iss(text);
    std::string word;
    int wordCount = 0;

    while (iss >> word) {
        wordCount++;
    }

    int charCount = text.length();
    std::string result = "文字数: " + std::to_string(charCount) + ", 単語数: " + std::to_string(wordCount);
    resultLabel->set_text(result);
}

int main() {
    customtkinter::set_appearance_mode("dark");
    customtkinter::set_default_color_theme("blue");

    customtkinter::Tk root;
    root.title("文字数カウンター");
    root.geometry("400x300");

    customtkinter::Label(root, text="文字数カウンター", font=("Helvetica", 16)).pack(pady=10);

    customtkinter::Textbox(root, placeholder_text="ここにテキストを入力してください", height=10, padx=15, pady=10).pack(pady=10);

    customtkinter::Label(root, text="文字数: 0, 単語数: 0", font=("Helvetica", 12)).pack(pady=10);

    customtkinter::Button(root, text="🔄 リセット", command=lambda: resetFields(inputField, resultLabel), width=10).pack(side=customtkinter::LEFT, padx=15);
    customtkinter::Button(root, text="📋 コピー", command=lambda: copyToClipboard(resultLabel.get_text()), width=10).pack(side=customtkinter::RIGHT, padx=15);

    root.mainloop();
}