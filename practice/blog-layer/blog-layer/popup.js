let changeColor = document.getElementById("changeColorButton");

chrome.storage.sync.get("color", ({ color }) => {
  changeColor.style.backgroundColor = color;
});

// When the button is clicked, inject setPageBackgroundColor into current page
changeColor.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: setPageBackgroundColor,
  });

  //여기서부터는 url 받아오는 작업
  //tab.url에는 익스텐션과 함께 보여지는 페이지의 url 주소가 담겨있음
  console.log(tab.url);  
});

// The body of this function will be executed as a content script inside the
// current page
function setPageBackgroundColor() {
  chrome.storage.sync.get("color", ({ color }) => {
    document.body.style.backgroundColor = color;
  });
}

let getSelectedTexts = document.getElementById('getSelectedTexts')


getSelectedTexts.addEventListener("click", () => {
  var sel = window.getSelection && window.getSelection();

  var range = window.getSelection().getRangeAt(0);
  var selectionContents = range.extractContents();

  console.log(selectionContents)
})

