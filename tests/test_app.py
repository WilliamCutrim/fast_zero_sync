from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (açao)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá mundo!'}


def test_read_root_html_deve_retornar_ok_e_ola_mundo():
    html = """
        \n    <html>\n      <head>\n        <title> Nosso olá mundo!</title>\n
                    </head>\n      <body>\n        
        <h1> Olá Mundo </h1>\n      </body>\n    </html>' == '\n        
        <html>\n        <head>\n            <title> Nosso olá mundo!</title>\n        
        </head>\n        <body>\n            <h1> Olá 
        Mundo </h1>\n        </body>\n        </html>\n    
    """
    client = TestClient(app)  # Arrange (organização)
    #breakpoint()
    response = client.get('/aa')  # Act (açao)
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.text == html  # assert

#test_read_root_html_deve_retornar_ok_e_ola_mundo()