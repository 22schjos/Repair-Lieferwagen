import streamlit as st

# --- 1. CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="Der Repair-Lieferwagen",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ASSETS (IMAGES & ICONS) ---
# We define the icons as SVG strings so they render exactly like Lucide-React
ICONS = {
    "wrench": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "calendar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
    "users": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "phone": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>',
    "map_pin": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
    "battery": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="6" width="18" height="12" rx="2" ry="2"></rect><line x1="23" y1="13" x2="23" y2="11"></line></svg>',
    "school": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 22v-4a2 2 0 1 0-4 0v4"/><path d="m18 10 4 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8l4-2"/><path d="M18 5v17"/><path d="m4 6 8-4 8 4"/><path d="M6 5v17"/><circle cx="12" cy="9" r="2"/></svg>',
    "camera": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>',
    "clock": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
}

IMAGES = {
    "hero": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=2021&auto=format&fit=crop",
    "team": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop",
    "repair": "https://images.unsplash.com/photo-1581092921461-eab62e97a780?q=80&w=2070&auto=format&fit=crop"
}

# --- 3. INJECT TAILWIND CSS ---
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* CSS Reset for Streamlit to look like a standard website */
        @import url('https://fonts.googleapis.com/css2?family=Verdana&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Verdana', sans-serif;
            background-color: #F3F4F6;
        }
        
        /* Hide standard Streamlit header and footer */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Remove default padding */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 5rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION LOGIC (Sidebar) ---
with st.sidebar:
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <div style="background-color: white; padding: 8px; border-radius: 8px; color: #005293;">
            {ICONS['wrench']}
        </div>
        <div>
            <h2 style="margin:0; color: #005293; font-size: 1.2rem;">Repair-Lieferwagen</h2>
            <p style="margin:0; font-size: 0.8rem; color: gray;">TFO Max Valier</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    active_tab = st.radio(
        "Navigation",
        ["Startseite", "Was wir reparieren", "Fahrplan", "Über Uns", "Kontakt"],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.info("💡 Nutzen Sie das Menü hier, um die Seite zu wechseln.")

# --- 5. CONTENT RENDERING ---

# >>> VIEW: STARTSEITE <<<
if active_tab == "Startseite":
    st.markdown(f"""
    <div class="max-w-4xl mx-auto px-4 py-8 md:py-12 space-y-12 animate-in fade-in duration-700">
        
        <section class="relative rounded-2xl shadow-xl overflow-hidden border border-blue-100 group hover:shadow-2xl transition-all duration-500 h-[500px] flex items-center justify-center">
            <div class="absolute inset-0 z-0">
                <img src="{IMAGES['hero']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-[2s]" />
                <div class="absolute inset-0 bg-gradient-to-br from-[#005293]/90 via-[#003366]/80 to-[#005293]/40 mix-blend-multiply"></div>
                <div class="absolute inset-0 bg-black/20"></div>
            </div>
            <div class="relative z-10 p-10 md:p-16 text-center text-white max-w-3xl">
                <h2 class="text-3xl md:text-5xl font-bold mb-6 leading-tight drop-shadow-lg">
                    Wir bringen Hilfe <br class="hidden md:block" />in Ihr Dorf.
                </h2>
                <p class="text-xl md:text-2xl mb-10 opacity-95 mx-auto leading-relaxed font-light drop-shadow-md">
                    Kostenlose Reparaturen, technische Unterstützung und ein offenes Ohr – <span class="font-semibold text-[#F2A900]">von Schülern für Senioren.</span>
                </p>
                <div class="bg-[#F2A900] text-white px-8 py-4 rounded-lg text-xl font-bold shadow-xl inline-flex items-center gap-3">
                   {ICONS['calendar']} Wann kommen wir?
                </div>
            </div>
        </section>

        <section class="prose prose-xl max-w-none text-slate-700">
            <h3 class="text-[#005293] font-bold text-3xl mb-4 flex items-center gap-3">
                <div class="p-2 bg-blue-50 rounded-lg text-[#F2A900]">{ICONS['school']}</div>
                Willkommen beim Repair-Lieferwagen!
            </h3>
            <p class="text-lg md:text-xl leading-relaxed">
                Manchmal sind es die kleinen Dinge, die im Alltag Sorgen bereiten: Der Toaster streikt, das Radio bleibt stumm oder der Föhn funktioniert nicht mehr. Oft fehlt nur ein geschickter Handgriff.
            </p>
            <p class="text-lg md:text-xl leading-relaxed mt-4">
                Genau dafür sind wir da. Unsere Schülerinnen und Schüler kommen mit dem Werkstatt-Bus direkt in Ihre Gemeinde.
            </p>
        </section>

        <section class="bg-white p-8 rounded-2xl shadow-md border border-gray-200 hover:shadow-xl transition-shadow duration-300">
             <h3 class="text-[#005293] font-bold text-3xl mb-10 text-center">So funktioniert es</h3>
             <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-xl shadow-md border-t-4 border-[#F2A900] hover:shadow-xl hover:-translate-y-2 transition-all duration-300">
                    <div class="text-[#005293] mb-4">
                        {ICONS['calendar']}
                    </div>
                    <h3 class="font-bold text-xl mb-2">1. Fahrplan prüfen</h3>
                    <p class="text-gray-600">Schauen Sie nach, wann unser Bus in Ihrem Dorf hält.</p>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-md border-t-4 border-[#005293] hover:shadow-xl hover:-translate-y-2 transition-all duration-300">
                    <div class="text-[#005293] mb-4">
                        {ICONS['map_pin']}
                    </div>
                    <h3 class="font-bold text-xl mb-2">2. Vorbeikommen</h3>
                    <p class="text-gray-600">Bringen Sie Ihr defektes Gerät einfach zum Standplatz.</p>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-md border-t-4 border-[#005293] hover:shadow-xl hover:-translate-y-2 transition-all duration-300">
                    <div class="text-[#005293] mb-4">
                        {ICONS['wrench']}
                    </div>
                    <h3 class="font-bold text-xl mb-2">3. Reparatur</h3>
                    <p class="text-gray-600">Wir reparieren kostenlos und freuen uns auf ein Gespräch.</p>
                </div>
             </div>
        </section>

        <div class="grid md:grid-cols-3 gap-6">
             <div class="bg-[#005293] text-white p-8 rounded-xl shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border-t-4 border-transparent hover:border-[#F2A900]">
                <h4 class="font-bold text-xl mb-3 border-b border-blue-400 pb-2 inline-block">Kostenlos</h4>
                <p class="opacity-90 leading-relaxed">Unser Service ist für Seniorinnen und Senioren gratis.</p>
             </div>
             <div class="bg-[#005293] text-white p-8 rounded-xl shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border-t-4 border-transparent hover:border-[#F2A900]">
                <h4 class="font-bold text-xl mb-3 border-b border-blue-400 pb-2 inline-block">Nachhaltig</h4>
                <p class="opacity-90 leading-relaxed">Reparieren statt Wegwerfen schont die Umwelt.</p>
             </div>
             <div class="bg-[#005293] text-white p-8 rounded-xl shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border-t-4 border-transparent hover:border-[#F2A900]">
                <h4 class="font-bold text-xl mb-3 border-b border-blue-400 pb-2 inline-block">Gemeinsam</h4>
                <p class="opacity-90 leading-relaxed">Wir lernen von Ihrer Lebenserfahrung, Sie profitieren von unserem Fachwissen.</p>
             </div>
        </div>

    </div>
    """, unsafe_allow_html=True)


# >>> VIEW: SERVICES (Repaired Snippet 1) <<<
elif active_tab == "Was wir reparieren":
    st.markdown(f"""
    <div class="max-w-4xl mx-auto px-4 py-8 md:py-12 space-y-8 animate-in fade-in duration-700">
        
        <div class="relative h-64 rounded-2xl overflow-hidden shadow-lg mb-8 group">
            <img src="{IMAGES['repair']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
            <div class="absolute inset-0 bg-gradient-to-t from-[#005293] to-transparent opacity-90"></div>
            <div class="absolute bottom-0 left-0 p-8 text-white">
                <h2 class="text-3xl md:text-4xl font-bold mb-2">Was können wir für Sie tun?</h2>
                <p class="text-xl opacity-90 max-w-2xl">Da wir Schüler einer technischen Schule sind, decken wir alle Bereiche ab, die wir auch im Unterricht lernen.</p>
            </div>
        </div>

        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-[#005293] hover:shadow-xl hover:translate-x-2 transition-all duration-300">
                <div class="flex items-start gap-4">
                    <div class="bg-blue-50 p-2 rounded-lg text-[#005293]">{ICONS['battery']}</div>
                    <div>
                        <h3 class="text-xl font-bold mb-2 text-[#005293]">Elektrische Kleingeräte</h3>
                        <p class="text-gray-600">Mixer, Toaster, Kaffeemühlen, alte Radios, Lampen.</p>
                    </div>
                </div>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-[#005293] hover:shadow-xl hover:translate-x-2 transition-all duration-300">
                <div class="flex items-start gap-4">
                    <div class="bg-blue-50 p-2 rounded-lg text-[#005293]">{ICONS['wrench']}</div>
                    <div>
                        <h3 class="text-xl font-bold mb-2 text-[#005293]">Mechanische Gegenstände</h3>
                        <p class="text-gray-600">Wackelige Stühle, klemmende Schubladen, Spielzeug.</p>
                    </div>
                </div>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-[#005293] md:col-span-2 hover:shadow-xl hover:translate-x-2 transition-all duration-300">
                 <div class="flex items-start gap-4">
                    <div class="bg-blue-50 p-2 rounded-lg text-[#005293]">{ICONS['phone']}</div>
                    <div>
                        <h3 class="text-xl font-bold mb-2 text-[#005293]">Technik-Hilfe</h3>
                        <p class="text-gray-600">Fragen zum Handy oder Tablet? Wir erklären es Ihnen in Ruhe.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="bg-orange-50 border-l-4 border-[#F2A900] p-6 rounded-r-xl">
             <h3 class="font-bold text-[#b45309] flex items-center gap-2">⚠️ Wichtiger Hinweis</h3>
             <p class="text-slate-700 mt-2">Großgeräte (Waschmaschinen etc.) können wir im Bus nicht reparieren. Keine Garantie.</p>
        </div>

    </div>
    """, unsafe_allow_html=True)


# >>> VIEW: SCHEDULE <<<
elif active_tab == "Fahrplan":
    st.markdown(f"""
    <div class="max-w-4xl mx-auto px-4 py-8 md:py-12 space-y-8 animate-in fade-in duration-700">
        <div class="mb-6">
            <h2 class="text-3xl md:text-4xl font-bold text-[#005293] mb-4">Wann sind wir in Ihrer Nähe?</h2>
            <p class="text-xl leading-relaxed text-slate-700">Hier finden Sie die nächsten Termine. Wir stehen meist auf dem Hauptplatz.</p>
        </div>

        <div class="bg-white rounded-xl shadow-lg overflow-hidden border border-gray-200">
            <table class="w-full min-w-[600px] text-left">
                <thead class="bg-[#005293] text-white">
                    <tr>
                        <th class="py-5 px-6 text-xl font-bold">Datum</th>
                        <th class="py-5 px-6 text-xl font-bold">Uhrzeit</th>
                        <th class="py-5 px-6 text-xl font-bold">Gemeinde</th>
                        <th class="py-5 px-6 text-xl font-bold">Standort</th>
                    </tr>
                </thead>
                <tbody class="text-lg md:text-xl text-slate-700">
                    <tr class="border-b border-gray-100 hover:bg-blue-50 transition-colors duration-200">
                        <td class="py-6 px-6 font-bold text-[#005293]">Mo, 12. Mai</td>
                        <td class="py-6 px-6">09:00 – 12:00</td>
                        <td class="py-6 px-6">Eppan</td>
                        <td class="py-6 px-6">Rathausplatz</td>
                    </tr>
                    <tr class="border-b border-gray-100 bg-gray-50 hover:bg-blue-50 transition-colors duration-200">
                        <td class="py-6 px-6 font-bold text-[#005293]">Mi, 14. Mai</td>
                        <td class="py-6 px-6">14:00 – 17:00</td>
                        <td class="py-6 px-6">Kaltern</td>
                        <td class="py-6 px-6">Marktplatz</td>
                    </tr>
                    <tr class="border-b border-gray-100 hover:bg-blue-50 transition-colors duration-200">
                        <td class="py-6 px-6 font-bold text-[#005293]">Fr, 16. Mai</td>
                        <td class="py-6 px-6">09:00 – 12:00</td>
                        <td class="py-6 px-6">Sarnthein</td>
                        <td class="py-6 px-6">Kirchplatz</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.button("📥 Plan als PDF herunterladen", use_container_width=True)


# >>> VIEW: ABOUT (Repaired Snippet 2) <<<
elif active_tab == "Über Uns":
    st.markdown(f"""
    <div class="max-w-4xl mx-auto px-4 py-8 md:py-12 space-y-8 animate-in fade-in duration-700">
        
        <div class="relative rounded-2xl overflow-hidden shadow-xl group cursor-pointer h-[400px]">
             <img src="{IMAGES['team']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
             <div class="absolute inset-0 bg-gradient-to-t from-[#005293] via-transparent to-transparent opacity-90"></div>
             <div class="absolute bottom-0 left-0 p-8 w-full">
                <div class="bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-xl text-white inline-block max-w-2xl">
                    <h3 class="text-3xl font-bold mb-2 flex items-center gap-3">
                        <span class="text-[#F2A900]">{ICONS['camera']}</span> Klasse 4Log A
                    </h3>
                    <p class="font-medium text-lg opacity-90">Die Schülerinnen und Schüler der TFO Max Valier bereit für den Einsatz.</p>
                </div>
             </div>
        </div>

        <h2 class="text-3xl md:text-4xl font-bold text-[#005293] mb-4 mt-8">Jung und Alt – Hand in Hand.</h2>

        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-8 rounded-xl shadow-sm border-l-4 border-[#F2A900]">
                <h3 class="font-bold text-2xl mb-3 text-[#005293]">Die Mission</h3>
                <p class="text-gray-700">Wir bauen Brücken zwischen den Generationen. Lernen findet nicht nur im Klassenzimmer statt.</p>
            </div>
            <div class="bg-white p-8 rounded-xl shadow-sm border-l-4 border-[#005293]">
                <h3 class="font-bold text-2xl mb-3 text-[#005293]">Das Team</h3>
                <p class="text-gray-700">Begleitet von unseren Fachlehrern lösen wir Probleme in der Praxis.</p>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)


# >>> VIEW: CONTACT (Repaired Snippet 3) <<<
elif active_tab == "Kontakt":
    st.markdown(f"""
    <div class="max-w-4xl mx-auto px-4 py-8 md:py-12 space-y-8 animate-in fade-in duration-700">
        <h2 class="text-3xl md:text-4xl font-bold text-[#005293] mb-4">Haben Sie noch Fragen?</h2>
        <p class="text-xl leading-relaxed mb-8 text-slate-700">Sind Sie unsicher, ob wir Ihr Gerät reparieren können? Rufen Sie uns gerne an.</p>

        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-gradient-to-br from-[#005293] to-[#003366] text-white p-8 rounded-xl shadow-lg relative overflow-hidden group hover:shadow-2xl hover:-translate-y-1 transition-all duration-300">
                <div class="absolute top-0 right-0 p-8 opacity-10 group-hover:scale-125 group-hover:rotate-12 transition-all duration-500" style="transform: scale(3);">
                    {ICONS['phone']}
                </div>
                <div class="flex flex-col items-center text-center gap-4 relative z-10">
                    <div class="bg-white text-[#005293] p-4 rounded-full shadow-lg group-hover:scale-110 transition-transform duration-300">
                        {ICONS['phone']}
                    </div>
                    <h3 class="text-2xl font-bold">Rufen Sie uns an</h3>
                    <p class="text-3xl md:text-4xl font-bold tracking-wider my-2 text-[#F2A900]">+39 0471 123 456</p>
                    <p class="opacity-90 text-lg flex items-center gap-2">{ICONS['clock']} Mo–Fr von 08:00 bis 12:00 Uhr</p>
                </div>
            </div>

            <div class="space-y-6">
                <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-[#F2A900] hover:shadow-xl transition-all group">
                    <h3 class="font-bold text-xl mb-2 flex items-center gap-3">
                        <span class="bg-blue-50 p-2 rounded-full text-[#005293] group-hover:bg-[#F2A900] group-hover:text-white transition-colors">{ICONS['map_pin']}</span>
                        Unser Standort
                    </h3>
                    <p class="text-gray-700">TFO Max Valier<br>Sorrentostraße 20<br>39100 Bozen</p>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-md border-l-4 border-[#F2A900] hover:shadow-xl transition-all group">
                    <h3 class="font-bold text-xl mb-2 flex items-center gap-3">
                        <span class="bg-blue-50 p-2 rounded-full text-[#005293] group-hover:bg-[#F2A900] group-hover:text-white transition-colors">{ICONS['users']}</span>
                        E-Mail
                    </h3>
                    <a href="mailto:info@repair-lieferwagen.it" class="text-[#005293] underline text-lg">info@repair-lieferwagen.it</a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- 6. FOOTER ---
st.markdown(f"""
<footer class="bg-[#1e293b] text-slate-300 py-10 mt-12 border-t-4 border-[#F2A900]" style="margin-left: -1rem; margin-right: -1rem; padding-left: 1rem; padding-right: 1rem;">
    <div class="max-w-6xl mx-auto px-4 text-center md:text-left flex flex-col md:flex-row justify-between items-center">
        <div class="mb-6 md:mb-0">
            <h4 class="font-bold text-lg text-white flex items-center justify-center md:justify-start gap-2">
                <span class="text-[#F2A900]">{ICONS['wrench']}</span>
                Der Repair-Lieferwagen
            </h4>
            <p class="opacity-70 text-sm mt-2">Ein Schulprojekt der TFO Max Valier für Südtirol.</p>
        </div>
        <div class="flex gap-4 md:gap-8 text-sm opacity-80">
            <span>Kontakt</span> | <span>Impressum</span> | <span>Datenschutz</span>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)
