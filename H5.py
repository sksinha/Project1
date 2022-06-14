import hydralit as hy

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp()
def my_home():
 hy.info('Hello from app1')

@app.addapp()
def app2():
 hy.info('Hello from app 2')
