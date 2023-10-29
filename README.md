<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="assets/img/favicon.png" rel="icon">
  <script src="https://kit.fontawesome.com/9650a62e47.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css">
  <link rel="stylesheet" type="text/css" href="./web/style.css">
  <title>Arduino Project</title>
</head>

<body>
  <header id="about">
    <nav id="navbar">
      <ul>
        <li><a href="#about"><i class="fa-solid fa-house"></i></a></li>
        <li><a href="#project-des"><i class="fa-regular fa-folder-open"></i></a></li>
        <li><a href="#video"><i class="fa-solid fa-play"></i></a></li>
        <li><a href="#members"><i class="fa-solid fa-user"></i></a></li>
      </ul>
    </nav>
    <div id="welcome-section" class="container">
      <h1 id="title"><div class="typewriter">Hello 👋, Teacher</div></h1><br>
      <p class="lead"><em>Let's see our project !</em></p>
    </div>
  </header>

  <section id ="project-des">
    <div class="project-des">
      <h1>PROJECT DESCRIPTION</h1>
        <img src ="./web/assets/arduino-uno.png" alt = "arduino" style="width:500px;height:500px;scale:80%;" ></image>
          <p>โปรเจ็กต์ของพวกเราได้มีการพัฒนาด้วยภาษา Arduino ซึ่งมีโครงสร้างมาจากภาษา C <br>และมีการผสมร่วมกันกับภาษา Python ในการทำ Face Recognition :)</p> 
          <p>โดยตัวภาษา C นั้นจะเป็นระบบแสดงผลที่มี LCD module เป็นจอในการแสดงผลขนาด 16x2</p>
          <img src = "./web/assets/LCD.png" style="width:600px;height:600px;scale:80%" ></image>
          <p>มีการใช้ Ultrasonic ในการตรวจจับคลื่นสะท้อนว่ามีวัตถุเคลื่อนผ่านเซนเซอร์หรือไม่</p>
          <img src = "./web/assets/Ultrasonic.png" style="width:600px;height:420px;scale:50%" ></image>
          <p>และ LED ที่ใช้ในการจำลองการแสดงผลว่าสแกนเสร็จสิ้นแล้วหรือไม่</p>
          <img src = "./web/assets/LED.png" style="width:600px;height:450px;scale:50%;margin-bottom: -60px;" ></image>
          <p>- - - - - - - - - - - - - - - - - - - - - -
          <br>ซึ่งระบบจะมีการทำงานเป็นขั้นตอนดังนี้
          <br>- - - - - - - - - - - - - - - - - - - - - -
          <br>1.ผู้ใช้ได้เพิ่มรูปภาพใบหน้าของตนเข้าไปเก็บไว้ในระบบ
          <br>2.เมื่อผู้ใช้เดินผ่าน Ultrasonic จะทำการตรวจจับวัตถุที่ผ่านเซนเซอร์
          <br>3.เมื่อผู้ใช้ทำการสแกนใบหน้าจะมีการตรวจเช็คว่าตรงกับข้อมูลที่เก็บไว้หรือไม่
          <br>4.LCD module แสดงข้อความต้อนรับ และ LED จะกระพริบจากสีแดงกลายเป็นสีน้ำเงินเป็นเวลา 2 วินาที</p>
        <br>
    </div>
  </section>

  <section id ="video">
    <div class="demo">
      <h3>DEMO</h3>
      <iframe class="youtube_frame" src="https://www.youtube.com/embed/E2YlqAT0WgU" allowfullscreen></iframe>
    </div>
  </section>

  <section id = "members"><br>
    <h3>MEMBERS</h3><br>
              <div class="contact-card">
                <img class="profile-img" src="./web/assets/member/Phowadol.jpg" style="width: 300px;height:300px;">
                <div class="column"><p class="name"> Phowadol  Sriphanna </p>
                <p class="detail">65070182</p></div>
                <img class="profile-img" src="./web/assets/member/Rawipon.jpg" style="width: 300px;height:300px;">
                <div class="column"><p class="name"> Rawipon Sa-ardpothong </p>
                <p class="detail">65070197</p></div>
                <img class="profile-img" src="./web/assets/member/Siriwit.jpg" style="width: 300px;height:300px;">
                <div class="column"><p class="name"> Siriwit Maneeshine </p>
                <p class="detail">65070215</p></div>
                <img class="profile-img" src="./web/assets/member/Atikun.jpg" style="width: 300px;height:300px;">
                <div class="column"><p class="name"> Atikun Pitsayo </p>
                <p class="detail">65070247</p></div>
              </div>
  </section>
</body>
</html> 
