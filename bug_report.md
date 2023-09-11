<table>
  <tbody>
    <tr>
      <td>ID</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Summary</td>
      <td>Параметр "phone" остается со значением "null" при ответе на запрос создания нового героя</td>
    </tr>
    <tr>
      <td>Priority</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td>Minor</td>
    </tr>
    <tr>
      <td>Status</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>Description</td>
      <td>Параметр "phone" остается со значением "null" в JSON ответе при создании нового героя. Ошибка выявлена в тестовом файле test_create_superhero.py, тест test_create_superhero</td>
    </tr>
    <tr>
      <td>Steps to reproduce</td>
      <td>
        Выполнить запрос <br>
        requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data, headers={"Content-Type": "application/json" })<br>
        data = {<br>
          "fullName": "Dr Pepper",<br>
          "birthDate": "2020-02-22",<br>
          "city": "New York",<br>
          "mainSkill": "Soda",<br>
          "gender": "M",<br>
          "phone": "+79456675588"<br>
        }
      </td>
    </tr>
    <tr>
      <td>Actual result</td>
      <td>{<br>
          "id": 490,  <br>
          "fullName": "Dr Pepper",  <br>
          "birthDate": "2020-02-22",  <br>
          "city": "New York",  <br>
          "mainSkill": "Soda",  <br>
          "gender": "M",   <br>
          "phone": None  <br>
          }</td>
    </tr>
    <tr>
      <td>Expected result</td>
      <td>{<br>
          "id": 490,  <br>
          "fullName": "Dr Pepper",  <br>
          "birthDate": "2020-02-22",  <br>
          "city": "New York",  <br>
          "mainSkill": "Soda",  <br>
          "gender": "M",   <br>
          "phone": "+79456675588"  <br>
          }</td>
    </tr>
  </tbody>
</table>


<table>
  <tbody>
    <tr>
      <td>ID</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Summary</td>
      <td>Код ответа = 500 при запросе на создание нового героя без параметра "mainSkill"</td>
    </tr>
    <tr>
      <td>Priority</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td>Minor</td>
    </tr>
    <tr>
      <td>Status</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>Description</td>
      <td>Код ответа = 500 при запросе на создание нового героя без параметра "mainSkill". Ошибка выявлена в тестовом файле test_create_superhero.py, тест test_create_superhero_without_mainskill</td>
    </tr>
    <tr>
      <td>Steps to reproduce</td>
      <td>
        Выполнить запрос <br>
        requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data, headers={"Content-Type": "application/json" })<br>
        пропустить параметр "mainSkill" в данных{<br>
        data = {<br>
          "fullName": "Thor",<br>
          "birthDate": "2020-02-22",<br>
          "city": "New York",<br>
          "gender": "M",<br>
          "phone": "+79456675588"<br>
        }
      </td>
    </tr>
    <tr>
      <td>Actual result</td>
      <td>{<br>
        "timestamp": "2023-09-11T17:51:39.156+0000", <br>
        "status": 500, <br>
        "error": "Internal Server Error", <br>
        "message": "could not execute statement; SQL [n/a]; constraint [null]; nested exception is org.hibernate.exception.ConstraintViolationException: could not execute statement", <br>
        "path": "/superheroes"<br>
        }
      </td>
    </tr>
    <tr>
      <td>Expected result</td>
      <td>{<br>
        "message": "Incorrect request data", <br>
        "code": "BAD_REQUEST"<br>
        }
      </td>
    </tr>
  </tbody>
</table>

