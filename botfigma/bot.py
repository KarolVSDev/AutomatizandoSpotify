from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):

        # programa que quer abrir no seu computador
        self.execute(r'C:\Users\blackoperation\Desktop\Spotify')
        
        
        if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
             self.not_found("pesquisar")
        self.click()
     
        self.paste("Garantido")
        self.enter()
        
        
        if not self.find( "album", matching=0.97, waiting_time=10000):
            self.not_found("album")
        self.click()
        
        
        if not self.find( "play", matching=0.97, waiting_time=10000):
            self.not_found("play")
        self.click()
        
        

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()




