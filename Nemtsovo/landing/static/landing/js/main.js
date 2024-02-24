const dialogs = document.querySelectorAll('dialog');

dialogs.forEach(dialog => {
  const closeBtn = dialog.querySelector('.close-dialog-btn');
  closeBtn.onclick = evt => {
    dialog.close();
    document.body.classList.remove('no-scroll');
  }
})

const openDialogBtns = document.querySelectorAll('[dialog]');
openDialogBtns.forEach(openDialogBtn => {
  const dialogId = openDialogBtn.getAttribute('dialog');
  if (!dialogId)
    return;

  const dialog = document.querySelector(`#${dialogId}`);
  if (!dialog)
    return;

  openDialogBtn.onclick = evt => {
    document.body.classList.add('no-scroll');
    dialog.showModal();
  }
});

const menuBtn = document.querySelector('#menu-btn');
const headerNavLinks = document.querySelector('.header-nav-links');
const navLinks = headerNavLinks.querySelectorAll('a');
const sideSocialLinks = document.querySelector('.side-social-links');

menuBtn.onclick = evt => {
  headerNavLinks.classList.toggle('menu-open');
  document.body.classList.toggle('no-scroll');
  sideSocialLinks?.classList.toggle('menu-open');
  window.scrollTo({top: 0, behavior: 'instant'});
}

navLinks.forEach(navLink => navLink.onclick = evt => {
  headerNavLinks.classList.remove('menu-open');
  document.body.classList.remove('no-scroll');
  sideSocialLinks.classList.remove('menu-open');
});