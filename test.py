from models import *



txt = """
<p>
У нас, вообще, интересная страна, вернее, люди, живущие на необъятных просторах. Кто-то пьет незамерзайку,
считая ее дешевой альтернативой алкогольной продукции. А кто-то льет в бачок омывателя недорогую водку,
считая, что так он экономит на покупке специальных жидкостей. Как бы было хорошо, если бы то что предназначено
для употребления внутрь пили, а то чем моют ветровое стекло лили в систему. Когда-нибудь такое время обязательно
настанет.
</p>
<h5>
Что входит в состав
</h5>
<p>
Как зачастую выбирают зимнюю омывающую жидкость? По цвету и надписи на этикетке, указывающей предельно допустимую
отрицательную температуру. При этом мало кто задумывается о составе, справится ли незамерзайка со своей основной 
функцией в морозы. Давайте все-таки более осознано подходить к выбору, а для этого надо знать состав жидкостей этого 
класса. В большинстве случаев в них входят:
</p>
<ul>
<li>
Подготовленная вода, занимающая значительную часть объема.
</li>
<li>
Спирт различных видов (метиловый, изопропиловый, этиловый). Именно из-за его концентрации зависит температура, при которой 
жидкость не замерзнет.
</li>
<li>
ПАВ (поверхностно-активные вещества), непосредственно отвечающие за отмывание грязи, расщепление жиров и органики.
</li>
<li>
Присадки-отдушки, позволяющие заменить резкий запах спирта на более приятные ароматы.
</li>
</ul>
<p>
Если какой-либо из компонентов не указан на этикетке, то высока вероятность того, что зимнюю омывающую жидкость разлили в 
ближайшем гараже. Броское название известного бренда еще не гарантирует качество, помните об этом. Нередко приходилось видеть 
автолюбителей с замерзшими емкостями в руках, прочесывающих рынок в поисках вчерашнего продавца. У них только одна радость — хорошо, 
что не успел залить в систему.
</p>
<h5>
Отличия незамерзайки на разных спиртах
</h5>
<p>
Они отличаются не только запахом, который легко убирается отдушками. Разница более кардинальна и не стоит упускать ее из вида. 
Смотрите в чем основные различия:
</p>
<ul>
<li>
Самый дешевый вариант — незамерзайка на метиловом спирте. Не стоит успокаивать себя тем, что в России продаже запрещена 
еще в 2000 году. Такие составы активно производятся в отдельных европейских странах, широко применяются при изготовлении 
подделок нашими умельцами. Основная опасность связана с высокой токсичностью паров такого спирта. Достаточно 1 миллиграмма
на кубометр воздуха, чтобы получить проблемы с центральной нервной системой. А при увеличении концентрации ущерб здоровью
может более серьезным, вплоть до летального исхода.
</li>
<li>
Чуть дороже омыватели на изопропиловом спирте. Вот у них действительно резкий неприятный запах, который трудно забить. 
Но проблема больше связана с высокой химической активностью таких составов. Они с легкостью разъедают уплотнения, силиконовые 
трубки, могут повредить ЛКП при попадании на поверхность.
</li>
<li>
Оптимальным вариантом считается незамерзайка на этиловом спирте (не стоит расслабляться, пить ее также нежелательно из-за 
других компонентов, входящих в состав). Эта жидкость обойдется дороже, но она отлично справляется с загрязнениями, не оказывает 
существенного влияния на компоненты системы.
</li>
</ul>
<p>
Вывод напрашивается сам, лучшее решение — незамерзающая жидкость для омывателя на основе этилового спирта.
</p>
<h5>
Какую все-таки выбрать
</h5>
<p>
Вы знаете, особой разницы между продукцией различных производителей нет. Хорошие жидкости предлагают бренды Liqui Moly, Hi-Gear, 
Sapfire, PINGO. Есть неплохие варианты и отечественных производителей, например, тот же Таймыр. Проблема заключается в большом количестве 
подделок. Поэтому чтобы не создать себе проблем, откажитесь от покупки на стихийных рынках, вдоль трасс, не покупайте незамерзайку и ходоков,
которых часто можно встретить на парковках и у гаражей.
</p>
<p>
Лучше переплатить лишних 50 рублей и потратить время на поездку в специализированный автомагазин. Ваша машина только скажет спасибо за такое
решение. Незамерзайка — не тот состав, на котором стоит экономить, тем более что и выигрыш по деньгам получается не такой уж и большой.
</p>
"""


# Content.create(
#         title="Зимняя омывающая жидкость — лить или не лить, вот в чем вопрос",
#         content=txt,
#         category=1,
#         slug="washer_fluid",
#         img="img/washer-fluid.jpg",
#         author=1,
#         is_published=True
#     )


#Content.update(category=2).where(Content.category == 1).execute()

#"internal_detailing"
#government_program
#new_mercedes_benz_avatar
#feedback_toyota
#beautiful_auto_number
#hyundai_creta_2020
#new_toyota_rav_5
#ditaling_inner_2
#washer_fluid
Content.update(category=3).where(Content.slug == "washer_fluid").execute()
