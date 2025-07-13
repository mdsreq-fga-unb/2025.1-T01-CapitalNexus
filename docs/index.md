# 🚀 Capital Nexus

Capital Nexus é uma solução web integrada para gestão operacional da equipe de competição Capital Rocket Team (CRT) 

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)

---


## 👥 Integrantes do Projeto

<div class="team-grid">

  <div class="team-card">
    <img src="assets/team/sophia.jpeg" alt="Sophia Silva" class="team-photo">
    <div class="team-info">
      <div class="name">Sophia Silva</div>
      <a href="https://github.com/sophiassilva" class="github-link" target="_blank">@sophiassilva</a>
    </div>
  </div>

  <div class="team-member">
    <img src="assets/team/christopher.jpeg" alt="Wanjo Christopher" class="team-photo">
    <div class="team-info">
      <div class="name">Wanjo Christopher</div>
      <a href="https://github.com/wChrstphr" class="github-link" target="_blank">@wChrstphr</a>
    </div>
  </div>

  <div class="team-member">
    <img src="assets/team/kaio.jpeg" alt="Kaio Macedo" class="team-photo">
    <div class="team-info">
      <div class="name">Kaio Macedo</div>
      <a href="https://github.com/bigkaio" class="github-link" target="_blank">@bigkaio</a>
    </div>
  </div>

  <div class="team-member">
    <img src="assets/team/victor.png" alt="Víctor Câmara" class="team-photo">
    <div class="team-info">
      <div class="name">Víctor Câmara</div>
      <a href="https://github.com/victorcamaraa" class="github-link" target="_blank">@victorcamaraa</a>
    </div>
  </div>

  <div class="team-member">
    <img src="assets/team/maria_clara.jpeg" alt="Maria Clara" class="team-photo">
    <div class="team-info">
      <div class="name">Maria Clara</div>
      <a href="https://github.com/mclarasenaa" class="github-link" target="_blank">@mclarasenaa</a>
    </div>
  </div>


  <div class="team-member">
    <img src="assets/team/pedro_henrique.jpeg" alt="Pedro Henrique" class="team-photo">
    <div class="team-info">
      <div class="name">Pedro Henrique</div>
      <a href="https://github.com/PhFariaa" class="github-link" target="_blank">@PhFariaa</a>
    </div>
  </div>

</div>

---

## ⚙️ Tecnologias Utilizadas
<div class="tech-architecture">

  <!-- Frontend Layer -->
  <div class="tech-layer">
    <div class="layer-title">Frontend</div>
    <div class="tech-list">
      <div class="tech-item">
        <div class="tech-icon" style="background: #f0db4f; color: #323330;">JS</div>
        <div>
          <div class="tech-name">JavaScript</div>
          <div class="tech-desc">Lógica e interatividade</div>
        </div>
      </div>
      <div class="tech-item">
        <div class="tech-icon" style="background: #e44d26;">H</div>
        <div>
          <div class="tech-name">HTML5</div>
          <div class="tech-desc">Estrutura de páginas</div>
        </div>
      </div>
      <div class="tech-item">
        <div class="tech-icon" style="background: #2965f1;">C</div>
        <div>
          <div class="tech-name">CSS3</div>
          <div class="tech-desc">Estilização e design</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Backend Layer -->
  <div class="tech-layer">
    <div class="layer-title">Backend</div>
    <div class="tech-list">
      <div class="tech-item">
        <div class="tech-icon" style="background: #3776ab;">Py</div>
        <div>
          <div class="tech-name">Python</div>
          <div class="tech-desc">Lógica de servidor</div>
        </div>
      </div>
      <div class="tech-item">
        <div class="tech-icon" style="background: #092e20; color: #fff;">Dj</div>
        <div>
          <div class="tech-name">Django</div>
          <div class="tech-desc">Framework web</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Database Layer -->
  <div class="tech-layer">
    <div class="layer-title">Banco de Dados</div>
    <div class="tech-list">
      <div class="tech-item">
        <div class="tech-icon" style="background: #336791; color: #fff;">DB</div>
        <div>
          <div class="tech-name">PostgreSQL</div>
          <div class="tech-desc">Banco de dados relacional</div>
        </div>
      </div>
    </div>
  </div>

</div>

### 🌐 **Arquitetura do Sistema**

```mermaid
graph LR
A[Frontend] -->|JavaScript| B(Navegador)
A -->|HTML/CSS| B
B -->|HTTP Requests| C[Backend]
C -->|Python| D[Django]
D -->|ORM| E[(PostgreSQL)]
E -->|Query Results| D
D -->|Responses| B
```
