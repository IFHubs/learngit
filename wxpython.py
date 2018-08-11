import wx
import matplotlib.pyplot as plt
def load(event):
	file = open(filename.GetValue())
	contents.SetValue(file.read())
	file.close()

def save(envet):
	file = open(filename.GetValue(), 'w')
	file.write(contents.GetValue())
	file.close()

def plot(event):
	X, Y = [], []
	content = [str(item) for item in contents.GetValue().strip().split('\n')]
	for line in content:
		x, y = [int(item) for item in line.strip().split()]
		X.append(x), Y.append(y)
	plt.plot(X, Y)
	plt.show()

app = wx.App()
win = wx.Frame(None, title='my first wx Window', size=(410, 335))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='Open')
loadButton.Bind(wx.EVT_BUTTON, load)
saveButton = wx.Button(bkg, label='Save')
saveButton.Bind(wx.EVT_BUTTON, save)
plotButton = wx.Button(bkg, label='Plot')
plotButton.Bind(wx.EVT_BUTTON, plot)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE|wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(plotButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vbox.Add(contents, proportion=1, 
	flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)
bkg.SetSizer(vbox)
win.Show()
app.MainLoop()