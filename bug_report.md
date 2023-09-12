<table>
  <tbody>
    <tr>
      <td>ID</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Summary</td>
      <td>Параметр "phone" остается со значением "null" в ответе на запрос создания нового героя</td>
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
      <td>Параметр "phone" остается со значением "null" в JSON ответе при создании нового героя</td>
    </tr>
    <tr>
      <td>Steps to reproduce</td>
      <td>
        Выполнить запрос: <br>
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
          "phone": null  <br>
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
      <td>Код ответа = 500 при запросе на создание нового героя без параметра "mainSkill". При отсуствии одного из других параметров возникает валидное сообщение, которое указано в Expected result</td>
    </tr>
    <tr>
      <td>Steps to reproduce</td>
      <td>
        Выполнить запрос: <br>
        requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data, headers={"Content-Type": "application/json" })<br>
        пропустить параметр "mainSkill" в данных:<br>
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


<table>
  <tbody>
    <tr>
      <td>ID</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Summary</td>
      <td>Не всегда можно получить информацию о герое</td>
    </tr>
    <tr>
      <td>Priority</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td>Major</td>
    </tr>
    <tr>
      <td>Status</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>Description</td>
      <td>Не всегда можно получить информацию о существующем герое</td>
    </tr>
    <tr>
      <td>Steps to reproduce</td>
      <td>
        1. Выполнить запрос на получение информации о всех героях:<br>
        requests.get('https://superhero.qa-test.csssr.com/superheroes')<br>
        2. Взять ID любого героя в ответе на запрос.<br>
        3. Выполнить запрос на получение информации о герое, подставив в {id} ID из п.2:<br>
        requests.get(f"https://superhero.qa-test.csssr.com/superheroes/{id}")<br>
        Если баг не воспроизвелся, повторить п.3 несколько раз. Ошибка возникает не всегда
      </td>
    </tr>
    <tr>
      <td>Actual result</td>
      <td>{id} - ID из п.2 в Steps to reproduce.<br>
        {<br>
        "message":"Superhero with id '{id}' was not found",<br>
        "code":"NOT_FOUND"<br>
        }<br>
      </td>
    </tr>
    <tr>
      <td>Expected result</td>
      <td>{id} - ID из п.2 в Steps to reproduce.<br>
        {<br>
        "id":{id},<br>
        "fullName":"Dragon",<br>
        "birthDate":"2020-02-22",<br>
        "city":"New York",<br>
        "mainSkill":"Soda",<br>
        "gender":"M",<br>
        "phone":"+79456675588"<br>
        }
      </td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td>ID</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Summary</td>
      <td>Герой всё ещё существует после выполнения запроса на удаление этого героя</td>
    </tr>
    <tr>
      <td>Priority</td>
      <td>Medium</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td>Major</td>
    </tr>
    <tr>
      <td>Status</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>Description</td>
      <td>Герой не всегда удаляется при вызове метода delete</td>
    </tr>
    <tr>
      <td>Steps to reproduce</td>
      <td>
        1. Выполнить запрос на создание героя:<br>
        requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data, headers={"Content-Type": "application/json"})<br>
        data = {<br>
          "fullName": "Dragon"<br>
          "birthDate": "2020-02-22",<br>
          "city": "New York",<br>
          "mainSkill": "Soda",<br>
          "gender": "M",<br>
          "phone": "+79456675588"<br>
        }<br>
        2. Взять его ID в ответе на запрос.<br>
        3. Выполнить запрос на удаление, подставив в {id} ID из п.2:<br>
        requests.delete(f"https://superhero.qa-test.csssr.com/superheroes/{id}")<br>
        4. Выполнить запрос на получение информации, подставив в {id} ID из п.2:<br>
        requests.get(f"https://superhero.qa-test.csssr.com/superheroes/{id}")<br>
        Если баг не воспроизвелся, попробовать еще раз. Ошибка возникает через раз
      </td>
    </tr>
    <tr>
      <td>Actual result</td>
      <td>{id} - ID из п.2 в Steps to reproduce.<br>
        {<br>
        "id":{id},<br>
        "fullName":"Dragon",<br>
        "birthDate":"2020-02-22",<br>
        "city":"New York",<br>
        "mainSkill":"Soda",<br>
        "gender":"M",<br>
        "phone":"+79456675588"<br>
        }
      </td>
    </tr>
    <tr>
      <td>Expected result</td>
      <td>{id} - ID из п.2 в Steps to reproduce.<br>
        {<br>
        "message": "Superhero with id '{id}' was not found",<br>
        "code": "NOT_FOUND"<br>
        }
      </td>
    </tr>
  </tbody>
</table>
