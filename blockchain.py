import hashlib
import json
from time import time

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, currentBlock):
        if(len(self.chain) == 0):
            self.createGensisBlock()
        currentBlock.previousHash = self.chain[-1].currentHash
        currentBlock.currentHash = currentBlock.calculateHash()
        self.chain.append(currentBlock)
    
    def createGensisBlock(self):
        genesisBlock = Block(0, time(), "No Previous Hash.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transactions", block.transactions)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        
        previousBlockHash = previousBlock.calculateHash()
        
        if(previousBlockHash != currentBlock.previousHash):
            return False
        
        return True
        
class Block:
    def __init__(self, index, timestamp, previousHash):
        self.index = index
        self.transactions = []
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
       
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp
        
        # Convert all the decimal data of a transaction into string using json.dumps() and store it in a variable .
        blockString =from web3 import Web3

# Call the API using the API url and store the connection in a variable
API_URL = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 =  Web3( Web3.HTTPProvider(API_URL))

# Define a function to get the gas price from the API
def getGasPrices():
    try:
        gasPrices={}
        gweiPrices={}
        etherPrices={}
        dollarPrices={}

        # Retrieve the current gas price from the API and store it in a variable.
        gasPrices["current"] = web3.eth.gas_price

        # Convert the gas prices as per their speed and store it.
        gasPrices["slow"] = int(gasPrices["current"] * 0.9)  
        gasPrices["standard"] = int(gasPrices["current"] * 1.0)   
        gasPrices["fast"] = int(gasPrices["current"] * 1.1)     
        gasPrices["rapid"] = int(gasPrices["current"] * 1.2)   
        
        # Convert gas prices from Wei to Gwei
        gweiPrices["current"] = web3.from_wei(gasPrices["current"], 'gwei')
        gweiPrices["slow"] = web3.from_wei(gasPrices["slow"], 'gwei')
        gweiPrices["standard"] = web3.from_wei(gasPrices["standard"], 'gwei')
        gweiPrices["fast"] = web3.from_wei(gasPrices["fast"], 'gwei')
        gweiPrices["rapid"] = web3.from_wei(gasPrices["rapid"], 'gwei')
        
        # Conversion of gas price into ether
        etherPrices["current"] = web3.from_wei(gasPrices["current"], 'ether')
        etherPrices["slow"] = web3.from_wei(gasPrices["slow"], 'ether')
        etherPrices["standard"] = web3.from_wei(gasPrices["standard"], 'ether')
        etherPrices["fast"] = web3.from_wei(gasPrices["fast"], 'ether')
        etherPrices["rapid"] = web3.from_wei(gasPrices["rapid"], 'ether')

        
        # Conversion of gas price into ether to dollars
        conversionRate = 1826
        dollarPrices["current"] = etherPrices["current"] * int(conversionRate)
        dollarPrices["slow"] = etherPrices["slow"] * int(conversionRate)
        dollarPrices["standard"] = etherPrices["standard"] * int(conversionRate)
        dollarPrices["fast"] = etherPrices["fast"] * int(conversionRate)
        dollarPrices["rapid"] =  etherPrices["rapid"] * int(conversionRate)
     
        return gasPrices, gweiPrices, etherPrices, dollarPrices

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None str(self.index) + str(timestamp) + str(self.previousHash) 
        return generateHash(blockString)

    def addTransaction(self, transaction):
        if transaction:
            self.transactions.append(transaction)
            if len(self.transactions) == 3:
                self.currentHash = self.calculateHash()
                return "Ready"
            return "Add more transactions"


       
