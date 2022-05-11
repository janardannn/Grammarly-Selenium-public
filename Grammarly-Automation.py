from grammarly import Grammarly
import os

  
class Grammarly_Files_Integration:
    
    def handle_file_input(self):
        
        while True:
            try:
                folder_path = input("Enter text files folder path: ").strip()

                if "\\" in folder_path:
                    folder_path = folder_path.replace("\\", "/")
                
                files = os.listdir(folder_path)
                
                print("Which file do you want to choose?\n")
                count = 2

                print("1) Select all files")
                for f in files:
                    print(f"{count}) {f}")
                    count+=1
                
                file_choice = int(input("\nEnter file number: ").strip())
                file_choice -= 2

                if file_choice == -1:
                    print("All files selected")
                    return [os.path.join(folder_path, k) for k in os.listdir(folder_path)]
                
                else:
                    print(f"\"{files[file_choice]}\" File selected")
                    return [os.path.join(folder_path, files[file_choice])]
            
            except FileNotFoundError:
                print("Wrong folder path")


    def breakdown_text_file(self,text_file):

            f = open(text_file, "r", encoding="utf-8")
            text = [k for k in f.readlines()]
            f.close()

            word_count = 0

            small_piece_data = []

            paragraphs = []
                    
            for line in text:
                
                if word_count < 70:
                    small_piece_data.append(line)
                    word_count += len(line.split())
                else:
                    paragraph = ""

                    for line in small_piece_data:
                        paragraph += line

                    paragraphs.append(paragraph)

                    word_count = 0

            return paragraphs

    
    def save_corrected_file(self,corrected_text,file_name_format):
        
        folder_path = "corrected_files/"

        file_name = file_name_format.split(".")[0]
        file_format = file_name_format.split(".")[1]

        out = open(f"{folder_path}/{file_name}.{file_format}", "w")
        out.write(corrected_text)
        out.close()

        print("File saved")


    
    def file_cycling(self,files):
        
        for f in files:

            document_url = self.get_document_url()

            print(f.split("\\")[-1] + " is being corrected")
            
            broken_down_file = self.breakdown_text_file(f)

            correct = []

            for paragraph in broken_down_file:

                corrected_text = self.run(paragraph)
                #self.grammar.driver.get(document_url)
                correct.append(corrected_text)
                self.grammar.clear_document()
            
            self.save_corrected_file(correct,f.split("\\")[-1])


    def activate_grammaly(self):
        self.grammar = Grammarly()
        self.grammar.login()
        
    def get_document_url(self):
        if self.grammar.driver.current_url == "https://app.grammarly.com/":
            document = self.grammar.open_new_file()
            return document
        else:
            self.grammar.driver.get("https://app.grammarly.com/")
            document = self.grammar.open_new_file()
            return document

    def run(self,text):

        self.grammar.enter_text(text)
        correct = self.grammar.identify_and_resolve_error()
        return correct

def main():

    grammar_bot = Grammarly_Files_Integration()
    
    files = grammar_bot.handle_file_input()
    
    grammar_bot.activate_grammaly()
    
    grammar_bot.file_cycling(files)


main()