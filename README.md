Автоматические контейнеры для игредиентов и зелий
=================================================

Мод предоставляет автоматические переносные контейнеры следующих двух видов.

1. Мешок для ингредиентов. В этот контейнер автоматически складываются ингредиенты.
2. Сундук для зелий. В этот контейнер автоматически складываются зелья.

Предоставляется по три экземпляра контейнера каждого вида (один можно использовать для стационарного хранения соответсвующих вещей в своём логове/лаборатории, второй носить с собой, третий - резервный).

После поключения соответствующего плагина, все контейнеры появятся в вашем инвентаре, готовые к использованию. Если какая-то разновидность контейнера вам не нужна, можно убрать соответствующий предмет, перетащив его в инвентаре на себя.

Чтобы воспользоваться контейнером, откройте инвентарь и выложите на пол (или на землю) этот контейнер, затем закройте инвентарь и дождитесь сообщения «Ингредиенты/Зелья выложены». Лучше выкладывать контейнер не под ноги, а в стороне - тогда вы точно не застряните в нём. После совершения описанных действий контейнер будет вести себя так же как обычные стацинарные контейнеры - вы можете класть или брать из него любые предметы. А при нажатии кнопки «Взять все» предметы из контейнера вместе с самим контейнером окажутся в вашем инвентаре.

При выкладывании контейнера в инвентарь автоматически добавляется его замена, чтобы вы могли оставить, при желании, первый контейнер в этом месте надолго. Исчезают «лишние» контейнеры также автоматически.

Установка
---------

1. Скопировать содержимое папки `Data Files` со всем содержимым в подпапку `Data Files` директории, куда установлен Morrowind (при необходимости, с заменой имеющихся файлов от более старой версии).

2. Подключить `A1_IngredientsBag_V1.esp`.

3. Загрузить игру, сохранить в новый слот.

Конфликты и ограничения
-----------------------

Иногда вылетает (по наблюдениям автора - очень-очень редко, но всё же бывает). Иногда (так же весьма редко, но бывает) при выкладывании контейнера из инвентаря соответствующие скрипты не срабатывают (нет сообщения о завершении операции и падения частоты кадров, которое указывало бы на то, что предметы перекладываются) - в таком случае нужно просто подобрать выложенный премет обратно (в отличие от нормальной ситуации он не будет работать как контейнер при активации, то есть он не откроется, а просто возьмётся) и повторить операцию. Иногда вместо одного контейнера в инвентаре оказывается два или три. Если их выложить и забрать обратно, это исправляется.

Некоторые операции (связанные с перекладыванием больших количеств предметов) могут занимать значительное время (до нескольких секунд).

Обратная связь
--------------

Автор будет рад увидеть ваши вопросы, пожелания, предложения и др. в своей почте [internalmike@gmail.com] или на гитхабе [https://github.com/A1-Triard/containers/issues].

Благодарности
-------------

Автор благодарит всех принимавших участие в создании и переводе фундаментального труда "Morrowind Scripting for Dummies", создателей и локализаторов расширителя скриптов MWSE, создателей редатора плагинов MWEdit, а также всех, кто принимал участие в создании легендарной игры Морровинд, но _не принимал_ участия в создании нелегендарных игр Скайрим и TES Online.