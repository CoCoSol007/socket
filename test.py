"""thread lancer
    client.send(self.data[key])
KeyError: None

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\soloi\AppData\Local\Programs\Python\Python310\lib\threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "c:\Users\soloi\Desktop\socket\constant.py", line 57, in run
    self.fonction(self.arg)
  File "c:\Users\soloi\Desktop\socket\serveur.py", line 88, in transfere_donné_envoi
    remove_player_in_data(self.all_conexion, client)
  File "c:\Users\soloi\Desktop\socket\constant.py", line 70, in remove_player_in_data
    data[keys].remove(player)
KeyError: None"""

            