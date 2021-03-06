# Автотесты на примере [интернет-магазина](http://automationpractice.com/index.php) созданного для практики в автоматическом тестировании
**Выбранная функциональность:** взаимодействие пользователя с корзиной покупателя 

**Тест-кейс №1: выдача товара по поисковому запросу**
* *Предусловие*: интересующий пользователя товар бывает в наличии в данном магазине
* *Шаги*:  
   * Ввести в поисковой строке название товара (в качестве примера можно ввести blouse или dress)
   * Нажать Enter
* *Ожидаемый результат*: сайт сформирует поисковую выдачу в соответствии с запросом
* *Результат тестирования*: ОК

**Тест-кейс №2: добавление товара в корзину**
* *Предусловие*: найден товар для покупки
* *Шаги*:  
   * Нажать на кнопку "Add to cart" возле выбранного товара
   * Нажать на кнопку "Proceed to checkout" в открывшемся окне
* *Ожидаемый результат*: товар оказался в корзине
* *Результат тестирования*: ОК

**Тест-кейс №3: удаление товара из корзины**
* *Предусловие*: у пользователя в корзине есть товар, который он хочет удалить
* *Шаги*:  
   * Перейти в корзину, нажав на кнопку "Cart" вверху сайта (если не в ней)
   * Нажать на кнопку "Delete" возле подлежащего удалению товара
* *Ожидаемый результат*: товар был удален из корзины
* *Результат тестирования*: ОК

**Тест-кейс №4: возвращение в магазин из пустой корзины**
* *Предусловие*: пустая корзина покупателя
* *Шаги*:  
   * Перейти в корзину, нажав на кнопку "Cart" вверху сайта (если не в ней)
   * Нажать лого
* *Ожидаемый результат*: пользователь переносится на главную поисковую страницу интернет-магазина
* *Результат тестирования*: ОК

**Тест-кейс №5: обновление количества товара в корзине**
* *Предусловие*: наличие товаров в корзине покупателя
* *Шаги*:  
   * Перейти в корзину, нажав на кнопку "Cart" вверху сайта (если не в ней)
   * Нажать кнопку "Plus" возле товара
   * Нажать кнопку "Minus" возле товара
* *Ожидаемый результат*: количества товара сначала увеличиться на 1, а потом уменьшиться на 1
* *Результат тестирования*: ОК

**Тест-кейс №6: возвращение в магазин после добавление товара в корзину**
* *Предусловие*: наличие товаров в корзине покупателя
* *Шаги*:  
   * Перейти в корзину, нажав на кнопку "Cart" вверху сайта (если не в ней)
   * Нажать кнопку "Continue shopping"
* *Ожидаемый результат*: пользователь переносится на главную поисковую страницу интернет-магазина
* *Результат тестирования*: ОК

