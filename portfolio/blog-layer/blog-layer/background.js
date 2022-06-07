let color = "#ACBABF";

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log("Default background color set to %cgreen", `color: ${color}`);
});


console.log('background.js 실행')

// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//   if(message.isBoxClicked){
//     chrome.tabs.query({active:true, lasFocusedPage: true}, tabs => {
//       const url = tabs[0].url;
//       console.log(url)
//     })
//   }
// })
