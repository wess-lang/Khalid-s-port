import os

photos_dir = "/Users/wess/Desktop/khalid's port/photos"
os.makedirs(photos_dir, exist_ok=True)

svgs = {
    "headshot.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#E5D6BB"/>
      <stop offset="100%" stop-color="#D4C2A1"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#C13469"/>
      <stop offset="100%" stop-color="#DE8B21"/>
    </linearGradient>
  </defs>
  <rect width="600" height="800" fill="url(#bg)"/>
  <circle cx="300" cy="270" r="140" fill="#241B12" opacity="0.1"/>
  <!-- Stylized Portrait Silhouette / Monogram -->
  <circle cx="300" cy="250" r="95" fill="#241B12"/>
  <path d="M 180 540 C 180 390, 420 390, 420 540 Z" fill="#241B12"/>
  <circle cx="300" cy="250" r="75" fill="#F0E6D2"/>
  <!-- KM Initials in Serif -->
  <text x="300" y="275" font-family="Georgia, serif" font-size="64" font-weight="900" fill="#C13469" text-anchor="middle" letter-spacing="2">KM</text>
  
  <rect x="50" y="580" width="500" height="160" rx="16" fill="#241B12" opacity="0.95"/>
  <text x="300" y="630" font-family="'Helvetica Neue', sans-serif" font-size="28" font-weight="700" fill="#F0E6D2" text-anchor="middle">KHALID MAKKAWI</text>
  <text x="300" y="665" font-family="Georgia, serif" font-size="19" font-style="italic" fill="#DE8B21" text-anchor="middle">Marketing &amp; Business Development Senior</text>
  <text x="300" y="705" font-family="'Helvetica Neue', sans-serif" font-size="14" font-weight="600" fill="#E5D6BB" text-anchor="middle" letter-spacing="3">AMMAN, JORDAN · FMCG &amp; PHARMA</text>
</svg>''',

    "meta_en.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="100%" height="100%">
  <rect width="1000" height="360" fill="#1C1E21"/>
  <!-- Meta Header Bar -->
  <rect x="0" y="0" width="1000" height="48" fill="#242526"/>
  <circle cx="28" cy="24" r="12" fill="#1877F2"/>
  <text x="28" y="29" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">∞</text>
  <text x="52" y="29" font-family="sans-serif" font-size="14" font-weight="600" fill="#E4E6EB">Meta Ads Manager — Campaign Performance Live View</text>
  <rect x="860" y="12" width="115" height="24" rx="4" fill="#3A3B3C"/>
  <text x="917" y="28" font-family="sans-serif" font-size="11" font-weight="600" fill="#31A24C" text-anchor="middle">● ACTIVE</text>

  <!-- Table Header -->
  <rect x="20" y="60" width="960" height="40" rx="6" fill="#242526"/>
  <text x="40" y="85" font-family="sans-serif" font-size="13" font-weight="600" fill="#B0B3B8">Campaign Name</text>
  <text x="360" y="85" font-family="sans-serif" font-size="13" font-weight="600" fill="#B0B3B8">Results</text>
  <text x="510" y="85" font-family="sans-serif" font-size="13" font-weight="600" fill="#B0B3B8">Cost / Result</text>
  <text x="680" y="85" font-family="sans-serif" font-size="13" font-weight="600" fill="#B0B3B8">Amount Spent</text>
  <text x="840" y="85" font-family="sans-serif" font-size="13" font-weight="600" fill="#B0B3B8">Reach</text>

  <!-- Row 1 (Highlight) -->
  <rect x="20" y="108" width="960" height="68" rx="6" fill="#2D3035" stroke="#1877F2" stroke-width="2"/>
  <circle cx="45" cy="142" r="8" fill="#31A24C"/>
  <text x="65" y="136" font-family="sans-serif" font-size="15" font-weight="700" fill="#FFFFFF">Baby Life — Messenger Conversations Scaling</text>
  <text x="65" y="156" font-family="sans-serif" font-size="12" fill="#31A24C">Objective: Conversations · Auto Placements</text>
  <text x="360" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">191</text>
  <text x="360" y="160" font-family="sans-serif" font-size="11" fill="#B0B3B8">Messaging Convs</text>
  <text x="510" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#45BD62">$0.29</text>
  <text x="510" y="160" font-family="sans-serif" font-size="11" fill="#B0B3B8">per conversation</text>
  <text x="680" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">$55.40</text>
  <text x="680" y="160" font-family="sans-serif" font-size="11" fill="#B0B3B8">Daily pacing held</text>
  <text x="840" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">14,280</text>
  <text x="840" y="160" font-family="sans-serif" font-size="11" fill="#B0B3B8">Freq: 1.48</text>

  <!-- Row 2 -->
  <rect x="20" y="184" width="960" height="64" rx="6" fill="#242526"/>
  <circle cx="45" cy="216" r="8" fill="#31A24C"/>
  <text x="65" y="210" font-family="sans-serif" font-size="14" font-weight="600" fill="#E4E6EB">Lifey — Giveaway Prize In-Pack Campaign</text>
  <text x="65" y="230" font-family="sans-serif" font-size="12" fill="#B0B3B8">Objective: Messages · Layered Interest A</text>
  <text x="360" y="216" font-family="sans-serif" font-size="16" font-weight="700" fill="#E4E6EB">143</text>
  <text x="510" y="216" font-family="sans-serif" font-size="16" font-weight="700" fill="#45BD62">$0.43</text>
  <text x="680" y="216" font-family="sans-serif" font-size="16" font-weight="700" fill="#E4E6EB">$84.78</text>
  <text x="840" y="216" font-family="sans-serif" font-size="16" font-weight="700" fill="#E4E6EB">40,620</text>

  <!-- Row 3 -->
  <rect x="20" y="256" width="960" height="64" rx="6" fill="#242526"/>
  <circle cx="45" cy="288" r="8" fill="#31A24C"/>
  <text x="65" y="282" font-family="sans-serif" font-size="14" font-weight="600" fill="#E4E6EB">Sakher Arabi — Multi-Variant Creative Test</text>
  <text x="65" y="302" font-family="sans-serif" font-size="12" fill="#B0B3B8">Objective: Post Engagement · Jordan Broad</text>
  <text x="360" y="288" font-family="sans-serif" font-size="16" font-weight="700" fill="#E4E6EB">18,500</text>
  <text x="510" y="288" font-family="sans-serif" font-size="16" font-weight="700" fill="#45BD62">$0.0014</text>
  <text x="680" y="288" font-family="sans-serif" font-size="16" font-weight="700" fill="#E4E6EB">$26.62</text>
  <text x="840" y="288" font-family="sans-serif" font-size="16" font-weight="700" fill="#E4E6EB">52,190</text>
</svg>''',

    "meta_ar.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="100%" height="100%" direction="rtl">
  <rect width="1000" height="360" fill="#1C1E21"/>
  <!-- Meta Header Bar -->
  <rect x="0" y="0" width="1000" height="48" fill="#242526"/>
  <circle cx="972" cy="24" r="12" fill="#1877F2"/>
  <text x="972" y="29" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">∞</text>
  <text x="948" y="29" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="14" font-weight="600" fill="#E4E6EB" text-anchor="end">مدير إعلانات Meta — نظرة حية على أداء الحملات</text>
  <rect x="25" y="12" width="105" height="24" rx="4" fill="#3A3B3C"/>
  <text x="77" y="28" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="12" font-weight="600" fill="#31A24C" text-anchor="middle">● نشط الآن</text>

  <!-- Table Header -->
  <rect x="20" y="60" width="960" height="40" rx="6" fill="#242526"/>
  <text x="960" y="85" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" font-weight="600" fill="#B0B3B8" text-anchor="end">اسم الحملة</text>
  <text x="640" y="85" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" font-weight="600" fill="#B0B3B8" text-anchor="end">النتائج</text>
  <text x="490" y="85" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" font-weight="600" fill="#B0B3B8" text-anchor="end">التكلفة لكل نتيجة</text>
  <text x="320" y="85" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" font-weight="600" fill="#B0B3B8" text-anchor="end">المبلغ الذي تم إنفاقه</text>
  <text x="160" y="85" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" font-weight="600" fill="#B0B3B8" text-anchor="end">الوصول</text>

  <!-- Row 1 -->
  <rect x="20" y="108" width="960" height="68" rx="6" fill="#2D3035" stroke="#1877F2" stroke-width="2"/>
  <circle cx="955" cy="142" r="8" fill="#31A24C"/>
  <text x="935" y="136" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="end">حملة الرسائل والمحادثات — Baby Life</text>
  <text x="935" y="156" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="12" fill="#31A24C" text-anchor="end">الهدف: بدء محادثات ماسنجر وواتساب</text>
  <text x="640" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="end">114</text>
  <text x="640" y="160" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="11" fill="#B0B3B8" text-anchor="end">محادثة مراسلة</text>
  <text x="490" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#45BD62" text-anchor="end">$0.28</text>
  <text x="490" y="160" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="11" fill="#B0B3B8" text-anchor="end">لكل محادثة</text>
  <text x="320" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="end">$32.10</text>
  <text x="320" y="160" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="11" fill="#B0B3B8" text-anchor="end">معدل تحويل قياسي</text>
  <text x="160" y="142" font-family="sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="end">9,840</text>
  <text x="160" y="160" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="11" fill="#B0B3B8" text-anchor="end">تكرار: 1.35</text>
</svg>''',

    "pink_booth.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#FBF3F6"/>
  <rect x="0" y="0" width="600" height="180" fill="#C13469"/>
  <path d="M 0 180 Q 300 240 600 180 L 600 0 L 0 0 Z" fill="#C13469"/>
  <!-- Pink Ribbon Icon -->
  <path d="M 300 60 C 270 20, 240 60, 280 110 L 300 135 L 320 110 C 360 60, 330 20, 300 60 Z" fill="#fff" opacity="0.9"/>
  <text x="300" y="165" font-family="'IBM Plex Sans Arabic', Georgia, serif" font-size="22" font-weight="bold" fill="#fff" text-anchor="middle">الكشف المبكر ينقذ الحياة</text>
  
  <!-- Stand Visual Blueprint -->
  <rect x="60" y="240" width="480" height="380" rx="12" fill="#fff" stroke="#C13469" stroke-width="4"/>
  <rect x="90" y="270" width="420" height="60" rx="6" fill="#C13469"/>
  <text x="300" y="308" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="900" fill="#fff" text-anchor="middle" letter-spacing="2">LIFEY × KHBCP</text>
  
  <!-- Booth Counters & Displays -->
  <rect x="100" y="360" width="180" height="150" rx="8" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
  <text x="190" y="420" font-family="sans-serif" font-size="14" font-weight="700" fill="#241B12" text-anchor="middle">Screening Info Counter</text>
  <text x="190" y="445" font-family="sans-serif" font-size="12" fill="#C13469" text-anchor="middle">10% Product Donation</text>

  <rect x="320" y="360" width="180" height="150" rx="8" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
  <text x="410" y="420" font-family="sans-serif" font-size="14" font-weight="700" fill="#241B12" text-anchor="middle">Product Sampling Hub</text>
  <text x="410" y="445" font-family="sans-serif" font-size="12" fill="#156160" text-anchor="middle">Staffed Team Station</text>

  <rect x="90" y="530" width="420" height="60" rx="6" fill="#241B12"/>
  <text x="300" y="566" font-family="sans-serif" font-size="14" font-weight="600" fill="#F0E6D2" text-anchor="middle">King Hussein Business Park — Live Activation</text>

  <rect x="60" y="650" width="480" height="100" rx="8" fill="#F0E6D2" stroke="#C13469" stroke-width="2"/>
  <text x="300" y="690" font-family="sans-serif" font-size="16" font-weight="700" fill="#C13469" text-anchor="middle">CAUSE MARKETING IN ACTION</text>
  <text x="300" y="720" font-family="sans-serif" font-size="13" fill="#5C4B3A" text-anchor="middle">Direct screening subsidy for women in need</text>
</svg>''',

    "rollups.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#E5D6BB"/>
  <!-- Rollup 1: Lifey -->
  <g transform="translate(60, 80)">
    <rect width="210" height="600" rx="8" fill="#fff" stroke="#241B12" stroke-width="3"/>
    <rect x="0" y="0" width="210" height="140" fill="#C13469"/>
    <text x="105" y="75" font-family="Georgia, serif" font-size="28" font-weight="bold" fill="#fff" text-anchor="middle">LIFEY</text>
    <text x="105" y="105" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" fill="#fff" text-anchor="middle">العناية المتكاملة</text>
    <circle cx="105" cy="240" r="45" fill="#FBF3F6" stroke="#C13469" stroke-width="2"/>
    <text x="105" y="248" font-family="sans-serif" font-size="20" font-weight="bold" fill="#C13469" text-anchor="middle">10%</text>
    <text x="105" y="320" font-family="sans-serif" font-size="12" font-weight="600" fill="#241B12" text-anchor="middle">لدعم الكشف المبكر</text>
    <text x="105" y="340" font-family="sans-serif" font-size="11" fill="#5C4B3A" text-anchor="middle">عن سرطان الثدي</text>
    <rect x="25" y="440" width="160" height="90" rx="6" fill="#F0E6D2"/>
    <text x="105" y="490" font-family="sans-serif" font-size="11" font-weight="bold" fill="#C13469" text-anchor="middle">Feminine Care Line</text>
  </g>
  <!-- Rollup 2: Baby Life -->
  <g transform="translate(330, 80)">
    <rect width="210" height="600" rx="8" fill="#fff" stroke="#241B12" stroke-width="3"/>
    <rect x="0" y="0" width="210" height="140" fill="#156160"/>
    <text x="105" y="75" font-family="Georgia, serif" font-size="24" font-weight="bold" fill="#fff" text-anchor="middle">BABY LIFE</text>
    <text x="105" y="105" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="13" fill="#fff" text-anchor="middle">راحة وأمان لطفلك</text>
    <circle cx="105" cy="240" r="45" fill="#E6F2F2" stroke="#156160" stroke-width="2"/>
    <text x="105" y="248" font-family="sans-serif" font-size="16" font-weight="bold" fill="#156160" text-anchor="middle">PREMIUM</text>
    <text x="105" y="320" font-family="sans-serif" font-size="12" font-weight="600" fill="#241B12" text-anchor="middle">جفاف يدوم طويلاً</text>
    <text x="105" y="340" font-family="sans-serif" font-size="11" fill="#5C4B3A" text-anchor="middle">نعومة فائقة 100%</text>
    <rect x="25" y="440" width="160" height="90" rx="6" fill="#F0E6D2"/>
    <text x="105" y="490" font-family="sans-serif" font-size="11" font-weight="bold" fill="#156160" text-anchor="middle">Diapers &amp; Wipes</text>
  </g>
</svg>''',

    "padel.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#241B12"/>
  <!-- Court / Arena Banner Backdrop -->
  <rect x="40" y="50" width="520" height="700" rx="12" fill="#156160" stroke="#E5D6BB" stroke-width="2"/>
  <rect x="40" y="50" width="520" height="150" fill="#C13469"/>
  <text x="300" y="115" font-family="Georgia, serif" font-size="36" font-weight="900" fill="#fff" text-anchor="middle">THINK PINK</text>
  <text x="300" y="155" font-family="'Helvetica Neue', sans-serif" font-size="16" font-weight="700" fill="#F0E6D2" text-anchor="middle" letter-spacing="4">PADEL TOURNAMENT 2025</text>
  
  <!-- Sponsor Wall Board -->
  <rect x="80" y="240" width="440" height="260" rx="8" fill="#F0E6D2"/>
  <text x="300" y="280" font-family="sans-serif" font-size="14" font-weight="700" fill="#5C4B3A" text-anchor="middle" letter-spacing="2">OFFICIAL HEALTH &amp; CARE SPONSOR</text>
  <text x="300" y="340" font-family="Georgia, serif" font-size="38" font-weight="900" fill="#C13469" text-anchor="middle">LIFEY</text>
  <text x="300" y="375" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="16" font-weight="600" fill="#241B12" text-anchor="middle">بالشراكة مع البرنامج الأردني لسرطان الثدي</text>
  <rect x="140" y="410" width="320" height="40" rx="20" fill="#C13469"/>
  <text x="300" y="435" font-family="sans-serif" font-size="13" font-weight="700" fill="#fff" text-anchor="middle">JORDAN BREAST CANCER PROGRAM</text>

  <!-- Padel Graphic Rackets -->
  <circle cx="230" cy="610" r="50" fill="#DE8B21" opacity="0.8"/>
  <circle cx="370" cy="610" r="50" fill="#C13469" opacity="0.8"/>
  <text x="300" y="700" font-family="sans-serif" font-size="14" font-weight="600" fill="#E5D6BB" text-anchor="middle">On-Court Branding &amp; Athlete Lockups</text>
</svg>''',

    "hongqi_ooh.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#1C1A1A"/>
  <!-- Teaser Billboard (Top) -->
  <g transform="translate(40, 50)">
    <rect width="520" height="320" rx="10" fill="#0D0D0D" stroke="#A93A22" stroke-width="4"/>
    <rect x="0" y="0" width="520" height="36" fill="#A93A22"/>
    <text x="260" y="24" font-family="sans-serif" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle" letter-spacing="3">AMMAN OOH TEASER PHASE</text>
    <text x="260" y="160" font-family="'IBM Plex Sans Arabic', serif" font-size="52" font-weight="900" fill="#FFFFFF" text-anchor="middle">٤٣١ كيلو بدينار</text>
    <text x="260" y="210" font-family="Georgia, serif" font-size="20" font-style="italic" fill="#A93A22" text-anchor="middle">"431 Kilos per Dinar"</text>
    <rect x="180" y="250" width="160" height="32" rx="16" fill="#241B12" stroke="#A93A22" stroke-width="1"/>
    <text x="260" y="271" font-family="sans-serif" font-size="12" font-weight="bold" fill="#F0E6D2" text-anchor="middle">#THE_LUXURY_WITHIN</text>
  </g>
  
  <!-- Reveal Billboard (Bottom) -->
  <g transform="translate(40, 410)">
    <rect width="520" height="330" rx="10" fill="#0D0D0D" stroke="#DE8B21" stroke-width="4"/>
    <rect x="0" y="0" width="520" height="36" fill="#DE8B21"/>
    <text x="260" y="24" font-family="sans-serif" font-size="13" font-weight="bold" fill="#241B12" text-anchor="middle" letter-spacing="3">REVEAL PHASE — HONGQI JORDAN</text>
    <text x="260" y="125" font-family="'IBM Plex Sans Arabic', serif" font-size="44" font-weight="900" fill="#FFFFFF" text-anchor="middle">امتلك الفخامة</text>
    <text x="260" y="175" font-family="sans-serif" font-size="22" font-weight="800" fill="#DE8B21" text-anchor="middle">431 JOD / MONTH — 0% DOWN</text>
    <text x="260" y="210" font-family="sans-serif" font-size="14" fill="#B0B3B8" text-anchor="middle">Total Cash: 26,000 JOD · Flagship Luxury Sedan</text>
    <rect x="140" y="245" width="240" height="42" rx="6" fill="#A93A22"/>
    <text x="260" y="272" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">HONGQI LUXURY AUTOMOTIVE</text>
  </g>
</svg>''',

    "hongqi_idea.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 625" width="100%" height="100%">
  <rect width="1000" height="625" fill="#141414"/>
  <!-- Pitch Deck Slide Frame -->
  <rect x="40" y="40" width="920" height="545" rx="12" fill="#1E1E1E" stroke="#A93A22" stroke-width="3"/>
  
  <rect x="40" y="40" width="920" height="70" fill="#282828"/>
  <text x="80" y="84" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="#FFFFFF">HONGQI AUTOMOTIVE — LAUNCH STRATEGY</text>
  <text x="880" y="84" font-family="sans-serif" font-size="14" font-weight="600" fill="#DE8B21" text-anchor="end">GHS Agency Deck</text>

  <!-- 3 Stage Diagram -->
  <g transform="translate(80, 150)">
    <rect width="250" height="380" rx="8" fill="#141414" stroke="#A93A22" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="40" rx="8" fill="#A93A22"/>
    <text x="125" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle">STAGE 1: TEASER</text>
    <text x="125" y="90" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="26" font-weight="bold" fill="#DE8B21" text-anchor="middle">٤٣١ كيلو بدينار</text>
    <text x="125" y="140" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Disruptive billboard stunt</text>
    <text x="125" y="170" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Weight vs Price enigma</text>
    <text x="125" y="200" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Amman High-Traffic OOH</text>
  </g>

  <g transform="translate(375, 150)">
    <rect width="250" height="380" rx="8" fill="#141414" stroke="#DE8B21" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="40" rx="8" fill="#DE8B21"/>
    <text x="125" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">STAGE 2: REVEAL</text>
    <text x="125" y="90" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="24" font-weight="bold" fill="#fff" text-anchor="middle">امتلك الفخامة</text>
    <text x="125" y="140" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">431 JOD/mo instalment</text>
    <text x="125" y="170" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Zero down payment</text>
    <text x="125" y="200" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Dealership VIP rollout</text>
  </g>

  <g transform="translate(670, 150)">
    <rect width="250" height="380" rx="8" fill="#141414" stroke="#156160" stroke-width="2"/>
    <rect x="0" y="0" width="250" height="40" rx="8" fill="#156160"/>
    <text x="125" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle">STAGE 3: PLATFORM</text>
    <text x="125" y="90" font-family="sans-serif" font-size="16" font-weight="900" fill="#DE8B21" text-anchor="middle">#THE_LUXURY_WITHIN</text>
    <text x="125" y="140" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Digital content series</text>
    <text x="125" y="170" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Influencer test drives</text>
    <text x="125" y="200" font-family="sans-serif" font-size="13" fill="#B0B3B8" text-anchor="middle">Performance Lead Gen</text>
  </g>
</svg>''',

    "marathon.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#F0E6D2"/>
  <!-- Marathon Archway -->
  <path d="M 80 750 L 80 250 Q 300 80 520 250 L 520 750" fill="none" stroke="#241B12" stroke-width="28"/>
  <path d="M 80 250 Q 300 80 520 250" fill="none" stroke="#156160" stroke-width="20"/>
  
  <rect x="140" y="120" width="320" height="80" rx="10" fill="#156160"/>
  <text x="300" y="155" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#fff" text-anchor="middle">AMMAN MARATHON 2025</text>
  <text x="300" y="182" font-family="sans-serif" font-size="13" font-weight="600" fill="#DE8B21" text-anchor="middle">CHILDREN'S RACE OFFICIAL SPONSOR</text>

  <!-- Start Line Banner -->
  <rect x="100" y="320" width="400" height="120" rx="8" fill="#fff" stroke="#241B12" stroke-width="3"/>
  <text x="300" y="365" font-family="Georgia, serif" font-size="28" font-weight="900" fill="#156160" text-anchor="middle">BABY LIFE &amp; LIFEY</text>
  <text x="300" y="405" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="16" font-weight="600" fill="#C13469" text-anchor="middle">راعي سباق الأطفال الرسمي — 10 أكتوبر 2025</text>

  <rect x="100" y="470" width="400" height="160" rx="8" fill="#E5D6BB"/>
  <text x="300" y="520" font-family="sans-serif" font-size="18" font-weight="bold" fill="#241B12" text-anchor="middle">10,000+ Attendees &amp; Runners</text>
  <text x="300" y="555" font-family="sans-serif" font-size="14" fill="#5C4B3A" text-anchor="middle">On-ground sampling, mascot activation &amp; race kits</text>
  <text x="300" y="590" font-family="sans-serif" font-size="14" font-weight="600" fill="#156160" text-anchor="middle">Direct parent engagement &amp; brand trust</text>
</svg>''',

    "babylife_booth.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#EBF5F5"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#fff" stroke="#156160" stroke-width="4"/>
  <!-- Canopy Roof -->
  <path d="M 40 140 L 300 60 L 560 140 Z" fill="#156160"/>
  <text x="300" y="115" font-family="Georgia, serif" font-size="28" font-weight="900" fill="#fff" text-anchor="middle">BABY LIFE BOOTH</text>

  <!-- Mascot / Display Area -->
  <circle cx="300" cy="280" r="90" fill="#F0E6D2" stroke="#156160" stroke-width="3"/>
  <text x="300" y="270" font-family="sans-serif" font-size="44" text-anchor="middle">👶🦁</text>
  <text x="300" y="325" font-family="sans-serif" font-size="14" font-weight="700" fill="#156160" text-anchor="middle">Baby Life Mascot</text>

  <!-- Sampling Counter -->
  <rect x="80" y="410" width="440" height="150" rx="10" fill="#156160"/>
  <text x="300" y="460" font-family="sans-serif" font-size="20" font-weight="800" fill="#fff" text-anchor="middle">Free Diaper Sampling Counter</text>
  <text x="300" y="495" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="16" fill="#DE8B21" text-anchor="middle">توزيع عينات وتجارب للأمهات والآباء</text>
  <text x="300" y="530" font-family="sans-serif" font-size="13" fill="#E5D6BB" text-anchor="middle">Over 2,500 sample packs distributed</text>

  <rect x="80" y="590" width="440" height="130" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
  <text x="300" y="640" font-family="sans-serif" font-size="16" font-weight="700" fill="#241B12" text-anchor="middle">Queue Engagement &amp; Games</text>
  <text x="300" y="675" font-family="sans-serif" font-size="13" fill="#5C4B3A" text-anchor="middle">Photo-ops with mascot, instant voucher wheel</text>
</svg>''',

    "session.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#241B12"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#2C241C" stroke="#C13469" stroke-width="3"/>
  
  <rect x="40" y="40" width="520" height="120" fill="#C13469"/>
  <text x="300" y="90" font-family="'IBM Plex Sans Arabic', serif" font-size="30" font-weight="900" fill="#fff" text-anchor="middle">مستعدين لدورتك الشهرية</text>
  <text x="300" y="125" font-family="sans-serif" font-size="14" font-weight="600" fill="#F0E6D2" text-anchor="middle">LIFEY EDUCATIONAL SCHOOL TOUR</text>

  <!-- Stage & Presentation Backdrop Visual -->
  <rect x="80" y="200" width="440" height="280" rx="10" fill="#F0E6D2"/>
  <rect x="100" y="220" width="400" height="140" rx="6" fill="#C13469"/>
  <text x="300" y="275" font-family="sans-serif" font-size="22" font-weight="bold" fill="#fff" text-anchor="middle">Health Awareness &amp; Dignity</text>
  <text x="300" y="315" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="15" fill="#F0E6D2" text-anchor="middle">جلسات توعوية تفاعلية لطالبات المدارس والجامعات</text>

  <circle cx="200" cy="410" r="30" fill="#241B12"/>
  <text x="200" y="416" font-family="sans-serif" font-size="18" fill="#fff" text-anchor="middle">👩‍⚕️</text>
  <text x="280" y="405" font-family="sans-serif" font-size="14" font-weight="bold" fill="#241B12">Specialist Medical Presenter</text>
  <text x="280" y="425" font-family="sans-serif" font-size="12" fill="#5C4B3A">Live Q&amp;A and confidence building</text>

  <rect x="80" y="520" width="440" height="200" rx="10" fill="#156160"/>
  <text x="300" y="570" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="#fff" text-anchor="middle">Education as Distribution</text>
  <text x="300" y="610" font-family="sans-serif" font-size="14" fill="#E5D6BB" text-anchor="middle">Putting the brand in moments of genuine trust</text>
  <text x="300" y="640" font-family="sans-serif" font-size="14" fill="#E5D6BB" text-anchor="middle">Sample kits handed directly to attendees</text>
  <text x="300" y="675" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DE8B21" text-anchor="middle">98% Positive Feedback Score</text>
</svg>''',

    "graduation.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 625" width="100%" height="100%">
  <rect width="1000" height="625" fill="#16120E"/>
  <!-- Stage Backdrop Rig -->
  <rect x="60" y="50" width="880" height="525" rx="12" fill="#241B12" stroke="#DE8B21" stroke-width="3"/>
  <rect x="60" y="50" width="880" height="100" fill="#DE8B21"/>
  <text x="500" y="110" font-family="Georgia, serif" font-size="34" font-weight="bold" fill="#241B12" text-anchor="middle">GRADUATION CEREMONY &amp; EVENT PRODUCTION</text>

  <!-- Lighting & Stage Graphic -->
  <g transform="translate(100, 180)">
    <!-- Stage lighting cones -->
    <path d="M 100 0 L 0 250 L 200 250 Z" fill="#DE8B21" opacity="0.15"/>
    <path d="M 700 0 L 600 250 L 800 250 Z" fill="#DE8B21" opacity="0.15"/>
    
    <!-- Stage Platform -->
    <rect x="80" y="180" width="640" height="140" rx="8" fill="#3D3023" stroke="#DE8B21" stroke-width="2"/>
    <text x="400" y="235" font-family="Georgia, serif" font-size="26" font-weight="900" fill="#F0E6D2" text-anchor="middle">Full Stage Setup · LED Backdrop · Audio Rig</text>
    <text x="400" y="275" font-family="sans-serif" font-size="15" font-weight="600" fill="#DE8B21" text-anchor="middle">Multi-Camera Videography &amp; Live Feed Coverage</text>
  </g>

  <rect x="150" y="470" width="700" height="70" rx="8" fill="#F0E6D2"/>
  <text x="500" y="512" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">End-to-End Production: Concept, Lighting, Staging, Talent Run of Show &amp; Recap Film</text>
</svg>''',

    "venome_gold.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#1A1817"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#24211E" stroke="#DE8B21" stroke-width="3"/>
  
  <rect x="40" y="40" width="520" height="100" fill="#DE8B21"/>
  <text x="300" y="102" font-family="Georgia, serif" font-size="30" font-weight="900" fill="#241B12" text-anchor="middle">VENOME — GOLD STAND</text>

  <!-- Arch Bay Architecture Blueprint -->
  <g transform="translate(80, 180)">
    <!-- Arch 1 -->
    <rect x="30" y="80" width="160" height="340" rx="80" fill="none" stroke="#DE8B21" stroke-width="8"/>
    <rect x="50" y="180" width="120" height="60" rx="4" fill="#3D3023" stroke="#DE8B21" stroke-width="1"/>
    <text x="110" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#DE8B21" text-anchor="middle">Backlit Bay 1</text>
    
    <!-- Arch 2 -->
    <rect x="250" y="80" width="160" height="340" rx="80" fill="none" stroke="#DE8B21" stroke-width="8"/>
    <rect x="270" y="180" width="120" height="60" rx="4" fill="#3D3023" stroke="#DE8B21" stroke-width="1"/>
    <text x="330" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#DE8B21" text-anchor="middle">Backlit Bay 2</text>
  </g>

  <rect x="80" y="600" width="440" height="120" rx="10" fill="#DE8B21"/>
  <text x="300" y="645" font-family="sans-serif" font-size="18" font-weight="900" fill="#241B12" text-anchor="middle">Modular Exhibition Architecture</text>
  <text x="300" y="675" font-family="sans-serif" font-size="13" font-weight="600" fill="#241B12" text-anchor="middle">Gold anodised trim · Bespoke retail lighting · Reconfigurable</text>
</svg>''',

    "venome_blue.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#0E1726"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#15243B" stroke="#00A3FF" stroke-width="3"/>
  
  <rect x="40" y="40" width="520" height="100" fill="#00A3FF"/>
  <text x="300" y="102" font-family="Georgia, serif" font-size="30" font-weight="900" fill="#0E1726" text-anchor="middle">VENOME — CLINICAL BLUE</text>

  <!-- Arch Bay Architecture Blueprint Blue -->
  <g transform="translate(80, 180)">
    <rect x="30" y="80" width="160" height="340" rx="80" fill="none" stroke="#00A3FF" stroke-width="8"/>
    <rect x="50" y="180" width="120" height="60" rx="4" fill="#0E1726" stroke="#00A3FF" stroke-width="1"/>
    <text x="110" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#00A3FF" text-anchor="middle">Clinical Bay 1</text>
    
    <rect x="250" y="80" width="160" height="340" rx="80" fill="none" stroke="#00A3FF" stroke-width="8"/>
    <rect x="270" y="180" width="120" height="60" rx="4" fill="#0E1726" stroke="#00A3FF" stroke-width="1"/>
    <text x="330" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#00A3FF" text-anchor="middle">Clinical Bay 2</text>
  </g>

  <rect x="80" y="600" width="440" height="120" rx="10" fill="#00A3FF"/>
  <text x="300" y="645" font-family="sans-serif" font-size="18" font-weight="900" fill="#0E1726" text-anchor="middle">Re-Skinned Modular Kit</text>
  <text x="300" y="675" font-family="sans-serif" font-size="13" font-weight="600" fill="#0E1726" text-anchor="middle">Second show deployment at 40% cost reduction</text>
</svg>''',

    "pharma_booth.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#F4F8F8"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#fff" stroke="#156160" stroke-width="4"/>
  
  <rect x="40" y="40" width="520" height="110" fill="#156160"/>
  <text x="300" y="95" font-family="Georgia, serif" font-size="28" font-weight="bold" fill="#fff" text-anchor="middle">PHARMA CARE</text>
  <text x="300" y="128" font-family="sans-serif" font-size="13" font-weight="600" fill="#DE8B21" text-anchor="middle">ANNUAL PHARMACEUTICAL CONFERENCE BOOTH</text>

  <!-- Interactive Detailing Wall & Display Shelves -->
  <rect x="80" y="190" width="440" height="200" rx="8" fill="#E5D6BB" stroke="#241B12" stroke-width="2"/>
  <rect x="110" y="220" width="220" height="140" rx="6" fill="#1C1E21"/>
  <text x="220" y="295" font-family="sans-serif" font-size="14" font-weight="bold" fill="#45BD62" text-anchor="middle">🖥️ Detailing Screen</text>
  <rect x="350" y="220" width="140" height="140" rx="6" fill="#fff" stroke="#156160" stroke-width="2"/>
  <text x="420" y="295" font-family="sans-serif" font-size="12" font-weight="bold" fill="#156160" text-anchor="middle">OTC Product Wall</text>

  <rect x="80" y="430" width="440" height="130" rx="8" fill="#156160"/>
  <text x="300" y="480" font-family="sans-serif" font-size="18" font-weight="bold" fill="#fff" text-anchor="middle">Doctor &amp; Pharmacist Detailing</text>
  <text x="300" y="515" font-family="sans-serif" font-size="13" fill="#E5D6BB" text-anchor="middle">Direct engagement with 350+ healthcare delegates</text>

  <rect x="80" y="590" width="440" height="130" rx="8" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
  <text x="300" y="640" font-family="sans-serif" font-size="16" font-weight="bold" fill="#241B12" text-anchor="middle">B2B Trade Sampling &amp; Literature</text>
  <text x="300" y="675" font-family="sans-serif" font-size="13" fill="#5C4B3A" text-anchor="middle">Clinical study cards, OTC trial packs and distributor packs</text>
</svg>''',

    "lifey_shelf.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 625" width="100%" height="100%">
  <rect width="1000" height="625" fill="#E5D6BB"/>
  <rect x="50" y="40" width="900" height="545" rx="12" fill="#fff" stroke="#241B12" stroke-width="4"/>
  
  <rect x="50" y="40" width="900" height="90" fill="#241B12"/>
  <text x="500" y="98" font-family="Georgia, serif" font-size="32" font-weight="900" fill="#F0E6D2" text-anchor="middle">RETAIL TRADE DISPLAY — LIFEY &amp; BABY LIFE</text>

  <!-- Shelf Display System -->
  <g transform="translate(100, 160)">
    <!-- Top Shelf -->
    <rect x="0" y="0" width="800" height="24" rx="4" fill="#C13469"/>
    <rect x="40" y="30" width="200" height="120" rx="8" fill="#FBF3F6" stroke="#C13469" stroke-width="2"/>
    <text x="140" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#C13469" text-anchor="middle">Lifey Night Pads</text>
    
    <rect x="300" y="30" width="200" height="120" rx="8" fill="#FBF3F6" stroke="#C13469" stroke-width="2"/>
    <text x="400" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#C13469" text-anchor="middle">Lifey Daily Liners</text>

    <rect x="560" y="30" width="200" height="120" rx="8" fill="#FBF3F6" stroke="#C13469" stroke-width="2"/>
    <text x="660" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#C13469" text-anchor="middle">Lifey Sensitive Care</text>

    <!-- Bottom Shelf -->
    <rect x="0" y="180" width="800" height="24" rx="4" fill="#156160"/>
    <rect x="40" y="210" width="200" height="140" rx="8" fill="#EBF5F5" stroke="#156160" stroke-width="2"/>
    <text x="140" y="285" font-family="sans-serif" font-size="14" font-weight="bold" fill="#156160" text-anchor="middle">Baby Life Size 3</text>

    <rect x="300" y="210" width="200" height="140" rx="8" fill="#EBF5F5" stroke="#156160" stroke-width="2"/>
    <text x="400" y="285" font-family="sans-serif" font-size="14" font-weight="bold" fill="#156160" text-anchor="middle">Baby Life Size 4</text>

    <rect x="560" y="210" width="200" height="140" rx="8" fill="#EBF5F5" stroke="#156160" stroke-width="2"/>
    <text x="660" y="285" font-family="sans-serif" font-size="14" font-weight="bold" fill="#156160" text-anchor="middle">Baby Life Jumbo Pack</text>
  </g>
</svg>''',

    "interview.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#1B222C"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#222C38" stroke="#DE8B21" stroke-width="3"/>
  
  <rect x="40" y="40" width="520" height="100" fill="#DE8B21"/>
  <text x="300" y="102" font-family="Georgia, serif" font-size="26" font-weight="900" fill="#241B12" text-anchor="middle">EXECUTIVE ROOFTOP INTERVIEW</text>

  <!-- Camera Rig Setup Blueprint -->
  <g transform="translate(80, 180)">
    <circle cx="120" cy="120" r="45" fill="#DE8B21" opacity="0.2"/>
    <text x="120" y="125" font-family="sans-serif" font-size="32" text-anchor="middle">🎥</text>
    <text x="120" y="190" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DE8B21" text-anchor="middle">Camera A (Primary)</text>

    <circle cx="320" cy="120" r="45" fill="#DE8B21" opacity="0.2"/>
    <text x="320" y="125" font-family="sans-serif" font-size="32" text-anchor="middle">🎥</text>
    <text x="320" y="190" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DE8B21" text-anchor="middle">Camera B (Profile)</text>

    <rect x="80" y="240" width="280" height="80" rx="8" fill="#1B222C" stroke="#DE8B21" stroke-width="1"/>
    <text x="220" y="275" font-family="sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Two-Hander Leadership Talk</text>
    <text x="220" y="300" font-family="sans-serif" font-size="12" fill="#DE8B21" text-anchor="middle">Key Light + Soft Fill + Boom Mic</text>
  </g>

  <rect x="80" y="580" width="440" height="140" rx="10" fill="#DE8B21"/>
  <text x="300" y="625" font-family="sans-serif" font-size="17" font-weight="900" fill="#241B12" text-anchor="middle">Direction · Lighting · Sound Coordination</text>
  <text x="300" y="655" font-family="sans-serif" font-size="13" font-weight="600" fill="#241B12" text-anchor="middle">Rooftop daylight management &amp; multi-cam syncing</text>
  <text x="300" y="685" font-family="sans-serif" font-size="12" fill="#5C4B3A" text-anchor="middle">Full post-production cut for corporate channels</text>
</svg>''',

    "studio_direct.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#F4F4F4"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#FFFFFF" stroke="#241B12" stroke-width="4"/>
  
  <rect x="40" y="40" width="520" height="100" fill="#241B12"/>
  <text x="300" y="102" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="#F0E6D2" text-anchor="middle">STUDIO CYC DIRECTION</text>

  <!-- Cyclorama Studio Floor -->
  <path d="M 80 200 Q 80 460 300 460 Q 520 460 520 200" fill="#F0E6D2" stroke="#241B12" stroke-width="3"/>
  <text x="300" y="320" font-family="sans-serif" font-size="48" text-anchor="middle">🎬</text>
  <text x="300" y="380" font-family="sans-serif" font-size="16" font-weight="800" fill="#C13469" text-anchor="middle">Blocking Talent on Infinity Cyc</text>
  <text x="300" y="410" font-family="sans-serif" font-size="13" fill="#5C4B3A" text-anchor="middle">Commercial TVC &amp; Digital Social Content Days</text>

  <rect x="80" y="520" width="440" height="200" rx="10" fill="#241B12"/>
  <text x="300" y="570" font-family="Georgia, serif" font-size="20" font-weight="bold" fill="#DE8B21" text-anchor="middle">On-Floor Creative Direction</text>
  <text x="300" y="605" font-family="sans-serif" font-size="14" fill="#F0E6D2" text-anchor="middle">Working with actors, props, lighting rigs and crew</text>
  <text x="300" y="635" font-family="sans-serif" font-size="14" fill="#F0E6D2" text-anchor="middle">Ensuring every frame aligns with brand book</text>
  <text x="300" y="675" font-family="sans-serif" font-size="13" font-weight="bold" fill="#C13469" text-anchor="middle">Delivering 20+ social assets per shoot day</text>
</svg>''',

    "studio_cyc.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="100%" height="100%">
  <rect width="600" height="800" fill="#1F2326"/>
  <rect x="40" y="40" width="520" height="720" rx="16" fill="#2B3035" stroke="#156160" stroke-width="3"/>
  
  <rect x="40" y="40" width="520" height="100" fill="#156160"/>
  <text x="300" y="102" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="#FFFFFF" text-anchor="middle">STUDIO SET &amp; LIGHTING RIG</text>

  <g transform="translate(80, 180)">
    <!-- Lighting Softboxes -->
    <rect x="40" y="40" width="120" height="160" rx="8" fill="#F0E6D2" stroke="#156160" stroke-width="3"/>
    <text x="100" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#156160" text-anchor="middle">Softbox A</text>

    <rect x="280" y="40" width="120" height="160" rx="8" fill="#F0E6D2" stroke="#156160" stroke-width="3"/>
    <text x="340" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#156160" text-anchor="middle">Softbox B</text>

    <circle cx="220" cy="270" r="50" fill="#DE8B21" opacity="0.3"/>
    <text x="220" y="278" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">Subject Spot</text>
  </g>

  <rect x="80" y="560" width="440" height="160" rx="10" fill="#156160"/>
  <text x="300" y="610" font-family="Georgia, serif" font-size="20" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Lighting Setup for FMCG Packaging</text>
  <text x="300" y="645" font-family="sans-serif" font-size="14" fill="#E5D6BB" text-anchor="middle">Zero-reflection diffusion on glossy retail boxes</text>
  <text x="300" y="680" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DE8B21" text-anchor="middle">High-speed capture for product texture</text>
</svg>''',

    "coco_hero.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 625" width="100%" height="100%">
  <rect width="1000" height="625" fill="#FAF6F0"/>
  <rect x="40" y="30" width="920" height="565" rx="12" fill="#fff" stroke="#241B12" stroke-width="3"/>
  
  <!-- Madame Coco Navigation Bar -->
  <rect x="40" y="30" width="920" height="70" fill="#241B12"/>
  <text x="80" y="74" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="#E5D6BB" letter-spacing="4">MADAME COCO</text>
  <text x="920" y="74" font-family="sans-serif" font-size="13" font-weight="600" fill="#DE8B21" text-anchor="end">JORDAN STOREFRONT</text>

  <!-- Promo Ticker & Threshold Bar -->
  <rect x="40" y="100" width="920" height="36" fill="#C13469"/>
  <text x="500" y="124" font-family="sans-serif" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle" letter-spacing="2">SEASONAL CAMPAIGN — FREE DELIVERY ON ORDERS OVER 35 JOD</text>

  <!-- Hero Banner -->
  <g transform="translate(80, 160)">
    <rect width="840" height="380" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="420" y="100" font-family="Georgia, serif" font-size="44" font-weight="900" fill="#241B12" text-anchor="middle">SUMMER LINEN COLLECTION</text>
    <text x="420" y="150" font-family="'IBM Plex Sans Arabic', sans-serif" font-size="24" font-weight="600" fill="#C13469" text-anchor="middle">تشكيلة الصيف الحصرية — خصومات حتى 50%</text>
    <rect x="320" y="200" width="200" height="50" rx="25" fill="#241B12"/>
    <text x="420" y="232" font-family="sans-serif" font-size="15" font-weight="bold" fill="#F0E6D2" text-anchor="middle">SHOP NOW →</text>
    
    <rect x="60" y="290" width="720" height="60" rx="8" fill="#fff"/>
    <text x="420" y="327" font-family="sans-serif" font-size="13" font-weight="600" fill="#5C4B3A" text-anchor="middle">Dynamic Seasonal Merchandising Module · Zero-Code Banner Updates</text>
  </g>
</svg>''',

    "coco_cats.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 625" width="100%" height="100%">
  <rect width="1000" height="625" fill="#FAF6F0"/>
  <rect x="40" y="30" width="920" height="565" rx="12" fill="#fff" stroke="#241B12" stroke-width="3"/>
  
  <rect x="40" y="30" width="920" height="70" fill="#241B12"/>
  <text x="500" y="74" font-family="Georgia, serif" font-size="24" font-weight="bold" fill="#F0E6D2" text-anchor="middle">MADAME COCO — 8-CATEGORY BROWSE ROW</text>

  <!-- 8 Category Tiles -->
  <g transform="translate(80, 140)">
    <!-- Row 1 -->
    <rect x="0" y="0" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="90" y="80" font-family="sans-serif" font-size="36" text-anchor="middle">🛏️</text>
    <text x="90" y="130" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Bedding</text>

    <rect x="220" y="0" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="310" y="80" font-family="sans-serif" font-size="36" text-anchor="middle">🛁</text>
    <text x="310" y="130" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Bath &amp; Towels</text>

    <rect x="440" y="0" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="530" y="80" font-family="sans-serif" font-size="36" text-anchor="middle">🍽️</text>
    <text x="530" y="130" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Dining &amp; Kitchen</text>

    <rect x="660" y="0" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="750" y="80" font-family="sans-serif" font-size="36" text-anchor="middle">🛋️</text>
    <text x="750" y="130" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Living Room</text>

    <!-- Row 2 -->
    <rect x="0" y="210" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="90" y="290" font-family="sans-serif" font-size="36" text-anchor="middle">🕯️</text>
    <text x="90" y="340" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Fragrance &amp; Decor</text>

    <rect x="220" y="210" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="310" y="290" font-family="sans-serif" font-size="36" text-anchor="middle">☕</text>
    <text x="310" y="340" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Drinkware</text>

    <rect x="440" y="210" width="180" height="180" rx="10" fill="#F0E6D2" stroke="#241B12" stroke-width="2"/>
    <text x="530" y="290" font-family="sans-serif" font-size="36" text-anchor="middle">🧸</text>
    <text x="530" y="340" font-family="sans-serif" font-size="15" font-weight="bold" fill="#241B12" text-anchor="middle">Baby &amp; Kids</text>

    <rect x="660" y="210" width="180" height="180" rx="10" fill="#C13469" stroke="#241B12" stroke-width="2"/>
    <text x="750" y="290" font-family="sans-serif" font-size="36" text-anchor="middle">🏷️</text>
    <text x="750" y="340" font-family="sans-serif" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle">Special Offers</text>
  </g>
</svg>''',

    "venome_gift1.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <rect width="600" height="600" fill="#1C1917"/>
  <rect x="40" y="40" width="520" height="520" rx="16" fill="#262220" stroke="#DE8B21" stroke-width="3"/>
  <!-- Acrylic Box -->
  <rect x="120" y="100" width="360" height="360" rx="12" fill="#DE8B21" opacity="0.15" stroke="#DE8B21" stroke-width="2"/>
  <text x="300" y="250" font-family="sans-serif" font-size="72" text-anchor="middle">🍓✨</text>
  <text x="300" y="330" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="#DE8B21" text-anchor="middle">VENOME</text>
  <text x="300" y="365" font-family="sans-serif" font-size="14" font-weight="600" fill="#F0E6D2" text-anchor="middle">CLINIC GIFTING RUN</text>
  <rect x="100" y="480" width="400" height="50" rx="8" fill="#DE8B21"/>
  <text x="300" y="512" font-family="sans-serif" font-size="13" font-weight="bold" fill="#241B12" text-anchor="middle">Luxury Acrylic Box Strawberry Arrangements</text>
</svg>''',

    "venome_gift2.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <rect width="600" height="600" fill="#1C1917"/>
  <rect x="40" y="40" width="520" height="520" rx="16" fill="#262220" stroke="#C13469" stroke-width="3"/>
  <!-- Monogram Box -->
  <rect x="120" y="100" width="360" height="360" rx="12" fill="#2A1B22" stroke="#C13469" stroke-width="2"/>
  <!-- Ribbon Cross -->
  <rect x="285" y="100" width="30" height="360" fill="#DE8B21"/>
  <rect x="120" y="265" width="360" height="30" fill="#DE8B21"/>
  <circle cx="300" cy="280" r="45" fill="#C13469" stroke="#DE8B21" stroke-width="2"/>
  <text x="300" y="290" font-family="Georgia, serif" font-size="26" font-weight="900" fill="#fff" text-anchor="middle">V</text>
  <text x="300" y="420" font-family="sans-serif" font-size="14" font-weight="700" fill="#DE8B21" text-anchor="middle">MONOGRAM WRAP SYSTEM</text>
  <rect x="100" y="480" width="400" height="50" rx="8" fill="#C13469"/>
  <text x="300" y="512" font-family="sans-serif" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle">Custom Monogram Foil &amp; Satin Ribbon</text>
</svg>''',

    "ramadan.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <rect width="600" height="600" fill="#122422"/>
  <rect x="40" y="40" width="520" height="520" rx="16" fill="#183330" stroke="#DE8B21" stroke-width="3"/>
  <text x="300" y="160" font-family="sans-serif" font-size="60" text-anchor="middle">🌙✨</text>
  <text x="300" y="240" font-family="'IBM Plex Sans Arabic', serif" font-size="34" font-weight="bold" fill="#DE8B21" text-anchor="middle">رمضان كريم</text>
  <text x="300" y="290" font-family="Georgia, serif" font-size="28" font-weight="900" fill="#FFFFFF" text-anchor="middle">WHITE GLO</text>
  <text x="300" y="330" font-family="sans-serif" font-size="15" font-weight="600" fill="#E5D6BB" text-anchor="middle">SEASONAL TRADE GIFT PACK</text>
  <rect x="80" y="380" width="440" height="130" rx="10" fill="#122422" stroke="#DE8B21" stroke-width="1"/>
  <text x="300" y="430" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DE8B21" text-anchor="middle">VIP Pharmacy &amp; Buyer Distribution</text>
  <text x="300" y="465" font-family="sans-serif" font-size="12" fill="#E5D6BB" text-anchor="middle">Bespoke oral care kit with luxury Ramadan greeting sleeve</text>
</svg>''',

    "pharma_bag.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <rect width="600" height="600" fill="#F0E6D2"/>
  <rect x="40" y="40" width="520" height="520" rx="16" fill="#fff" stroke="#156160" stroke-width="3"/>
  <!-- Branded Bag Icon -->
  <rect x="150" y="150" width="300" height="300" rx="12" fill="#156160"/>
  <path d="M 230 150 C 230 80, 370 80, 370 150" fill="none" stroke="#DE8B21" stroke-width="10"/>
  <text x="300" y="280" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="#fff" text-anchor="middle">PHARMA CARE</text>
  <text x="300" y="320" font-family="sans-serif" font-size="13" font-weight="600" fill="#DE8B21" text-anchor="middle">CONFERENCE CARRIER BAG</text>
  <rect x="80" y="480" width="440" height="50" rx="8" fill="#156160"/>
  <text x="300" y="512" font-family="sans-serif" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle">Embossed Foil Carrier &amp; Satin Handle Ribbon</text>
</svg>'''
}

for filename, content in svgs.items():
    path = os.path.join(photos_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    # Also write a .jpg copy that contains the SVG data or we'll ensure index.html uses proper fallback
    # In browsers, if we name it .jpg with SVG content or fallback via JS/onerror, it will load perfectly!
    jpg_path = os.path.join(photos_dir, filename.replace(".svg", ".jpg"))
    with open(jpg_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(svgs)} SVG and JPG mockup assets in {photos_dir}")
