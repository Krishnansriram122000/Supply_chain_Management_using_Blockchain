from flask import *
import datetime
import hashlib
class Block:
	blockno=0
	data=None
	next=None
	hash=None
	nonce=0
	amount=0
	previoushash=0x0
	timestamp=datetime.datetime.now()
	def __init__(self,data,amount):
		self.data=data
		self.amount=amount
	def hash(self):
		h=hashlib.sha256()
		h.update(
		str(self.blockno).encode('utf-8')+
		str(self.data).encode('utf-8')+
		str(self.amount).encode('utf-8')+
		str(self.previoushash).encode('utf-8')+
		str(self.nonce).encode('utf-8')+
		str(self.timestamp).encode('utf-8')
		)
		return h.hexdigest()
	def __str__(self):
		return "DATA: " +str(self.data) +" block hash:" + str(self.hash()) +"  block no :" + str(self.blockno)

app = Flask(__name__)

class blockchain:
	block=Block("Genesis Block",0)
	maxnonce=2**32
	diff=10
	target=2**(256-diff)
	head=block
	def add(self,block):
		block.previoushash=self.block.hash()
		block.blockno=self.block.blockno+1
		self.block.next=block
		self.block=self.block.next
	def mine(self,block):
		for n in range(self.maxnonce):
			if int(block.hash(),16) <= self.target :
				self.add(block)
				
				break
			else :
				block.nonce+=1
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        x=int(request.form['content123'])
        krish.mine(Block(str(task_content),(x)))
        return redirect('/')
    else:
    	kri=[]
    	t=krish.head
    	j=Block('just',9)
    	j=krish.head
    	while t!=None:
    		print(t)
    		j=t
    		t=t.next
    		kri.append(j)
    	return render_template('index.html',tasks=kri)
    		

if __name__ == "__main__":
    krish=blockchain()
    app.run(debug=True)