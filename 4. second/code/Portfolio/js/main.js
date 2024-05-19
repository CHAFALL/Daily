function toggleMenu() {
  const $navMenu = document.getElementById('nav__menu');
  // 이런것도 가능하구나~
  $navMenu.classList.toggle('show');
}

function handleFloatingButton() {
  const $floatingButton = document.getElementById('floating-button');

  $floatingButton.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      // behavior: 'smooth',
    });
  });
}

function init() {
  const $navToggle = document.getElementById('nav-toggle');
  $navToggle.addEventListener('click', () => {
    // Menu Toggle
    toggleMenu();
  });

  // 이거 좋다.
  const $navLinkList = document.querySelectorAll('.nav__link');
  $navLinkList.forEach((el) => el.addEventListener('click', toggleMenu));

  handleFloatingButton();
}

init();

const options = {
  // 언제쯤이면 감지가 되었다고 판단을 할건지 정의 가능(0 ~ 1)
  threshold: 1,
};

// 관찰자 만들기
// 콜백 함수의 파라미터로 교차된 정보들이 넘어온다.
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    const sectionId = entry.target.id;
    if (entry.isIntersecting) {
      // 앵커 태그를 찾아서 대입
      // href가 포함을 하냐(*=)
      document
        .querySelector(`.nav__link[href*=${sectionId}]`)
        .classList.add('active-link');

      // 현재놈을 제외하고 다 들고옴
      const $items = document.querySelectorAll(
        `.nav__link:not([href*=${sectionId}])`,
      );
      $items.forEach((el) => el.classList.remove('active-link'));
    }
  });
}, options);

// 만든 관찰자가 무엇을 관찰하도록 할지 정의해줌.
const $sectionList = document.querySelectorAll('.section');
$sectionList.forEach((el) => observer.observe(el));

// observer.observe(el) => 뭐를 관찰할꺼니??

// $는 그냥 엘리먼트의 네이밍 룰임 (J쿼리를 쓴다면 $로 네이밍 하면 헷갈리므로 안됨.)

// JS는 id를 통해서 조회를 함

// 무한 스크롤도 IntersectionObserver를 이용해서 구현 가능.

const scrollReveal = ScrollReveal({
  // 애니메이션이 시작될 위치
  origin: 'top',
  // 애니메이션이 이동할 거리
  distance: '60px',
  // 애니메이션의 지속시간
  duration: 1000,
  // 애니메이션이 시작되기 전의 지속시간
  delay: 100,
});

scrollReveal.reveal(
  '.home__data, .about__img, .skills__subtitle, .skills__text',
);
scrollReveal.reveal('.home__img, .about__data, .skills__img', { delay: 200 });
scrollReveal.reveal('.skills__data, .work__link, .contact__input', {
  interval: 100,
});

// interval: 도미노 식으로 구현.

const typeit = new TypeIt('#typeit', {
  speed: 70,
  startDelay: 1300,
  waitUntilVisible: true,
});

typeit
  .type('안녕하세요!<br />')
  .type(
    '<strong class="home__title-color">웹 풀스택 / 게임 개발자</strong><br />',
  )
  .type('<strong class="home__title-color">CHAFA</strong>', { delay: 300 })
  .delete(5, { delay: 300 })
  .type('<strong class="home__title-color">전근렬</strong>입니다!')
  .go();
