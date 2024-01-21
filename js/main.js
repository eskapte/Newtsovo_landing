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
})