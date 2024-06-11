  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBaDJtG0iU-mcSt3KegXPtSczV_TJhBWKQ",
    authDomain: "zoomb-os.firebaseapp.com",
    projectId: "zoomb-os",
    storageBucket: "zoomb-os.appspot.com",
    messagingSenderId: "880723983774",
    appId: "1:880723983774:web:7911124c842f0dcdd9aa8f",
    measurementId: "G-X6M9XMR7E9",
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  console.log("aqui chegou no cdigo");
  const analytics = getAnalytics(app);
  const storage = getStorage(app);