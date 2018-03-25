import psycopg2
from bottle import route, run, request

DSN = 'dbname=email_senders user=postgres host=db'
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

def register_message(assunto, message):
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute(SQL, (assunto, message))
    conn.commit()
    cur.close()
    conn.close()

    print('Mensagem registrada')

@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')

    register_message(assunto, mensagem)

    return "Mensagem infilerada! Asssunto: {} Mensagem: {}".format(
        assunto, mensagem
    )

if __name__ == '__main__': run(host='0.0.0.0', port=8081, debug=True)