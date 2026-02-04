<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Der Repair-Lieferwagen - TFO Max Valier Projekt</title>
    <style>
        /* CSS Variables for consistent theming */
        :root {
            --primary-blue: #005293;
            --accent-yellow: #F2A900;
            --background-light: #F3F4F6;
            --text-dark: #1e293b;
            --text-slate: #475569;
            --white: #ffffff;
            --blue-dark: #004074;
            --blue-darker: #00305a;
            --blue-gradient-start: #005293;
            --blue-gradient-middle: #003366;
            --blue-gradient-end: #005293;
            --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            --transition: all 0.3s ease-in-out;
            --border-radius: 1rem;
            --border-radius-lg: 1.5rem;
        }
        
        /* Base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Verdana', sans-serif;
            background-color: var(--background-light);
            color: var(--text-dark);
            line-height: 1.6;
            min-height: 100vh;
        }
        
        ::selection {
            background-color: var(--accent-yellow);
            color: white;
        }
        
        .container {
            max-width: 88rem;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
        
        /* Header & Navigation */
        header {
            background-color: var(--primary-blue);
            color: var(--white);
            position: sticky;
            top: 0;
            z-index: 50;
            box-shadow: var(--shadow-lg);
            border-bottom: 4px solid var(--accent-yellow);
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            cursor: pointer;
            transition: var(--transition);
        }
        
        .logo-icon {
            background-color: var(--white);
            padding: 0.5rem;
            border-radius: 0.5rem;
            color: var(--primary-blue);
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
        }
        
        .logo-icon:hover {
            transform: scale(1.1) rotate(6deg);
        }
        
        .logo-text h1 {
            font-size: 1.25rem;
            font-weight: 700;
            line-height: 1.25;
            letter-spacing: -0.025em;
            transition: var(--transition);
        }
        
        .logo-text p {
            font-size: 0.875rem;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.85);
            transition: var(--transition);
        }
        
        .logo:hover .logo-text h1 {
            color: rgba(255, 255, 255, 0.9);
        }
        
        .logo:hover .logo-text p {
            color: var(--white);
        }
        
        .nav-desktop {
            display: none;
            gap: 0.5rem;
        }
        
        .nav-item {
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            font-size: 1.125rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--white);
            background: none;
            border: none;
            cursor: pointer;
            transition: var(--transition);
        }
        
        .nav-item:hover {
            background-color: var(--blue-dark);
            transform: scale(1.05);
        }
        
        .nav-item.active {
            background-color: var(--white);
            color: var(--primary-blue);
            box-shadow: var(--shadow-md);
            transform: translateY(2px);
            position: relative;
        }
        
        .nav-item.active::after {
            content: '';
            position: absolute;
            bottom: -6px;
            left: 0;
            right: 0;
            height: 4px;
            background-color: var(--accent-yellow);
        }
        
        .mobile-menu-btn {
            background: none;
            border: none;
            color: var(--white);
            background-color: var(--blue-dark);
            padding: 0.5rem;
            border-radius: 0.5rem;
            cursor: pointer;
            transition: var(--transition);
        }
        
        .mobile-menu-btn:hover {
            background-color: var(--blue-darker);
        }
        
        .mobile-menu {
            display: none;
            background-color: var(--blue-dark);
            border-top: 1px solid rgba(0, 82, 147, 0.5);
            padding: 1rem 0;
        }
        
        .mobile-menu.active {
            display: block;
        }
        
        .mobile-nav-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100%;
            padding: 1rem;
            background: none;
            border: none;
            color: var(--white);
            font-size: 1.25rem;
            font-weight: 500;
            text-align: left;
            cursor: pointer;
            transition: var(--transition);
            border-radius: 0.75rem;
            margin: 0.5rem 1rem;
        }
        
        .mobile-nav-item:hover {
            background-color: var(--blue-darker);
        }
        
        .mobile-nav-item.active {
            background-color: var(--accent-yellow);
            color: var(--white);
            box-shadow: var(--shadow-md);
        }
        
        /* Main Content */
        main {
            max-width: 64rem;
            margin: 0 auto;
            padding: 2rem 1.5rem 4rem;
        }
        
        .view {
            display: none;
            animation: fadeIn 0.7s ease-out forwards;
        }
        
        .view.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .hero {
            position: relative;
            height: 500px;
            border-radius: var(--border-radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-xl);
            border: 1px solid rgba(0, 82, 147, 0.3);
            cursor: pointer;
            transition: var(--transition);
        }
        
        .hero:hover {
            box-shadow: var(--shadow-xl);
        }
        
        .hero-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 2s ease-out;
        }
        
        .hero:hover .hero-img {
            transform: scale(1.05);
        }
        
        .hero-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to bottom right, 
                rgba(0, 82, 147, 0.9) 0%, 
                rgba(0, 51, 102, 0.8) 50%, 
                rgba(0, 82, 147, 0.4) 100%);
            mix-blend-mode: multiply;
        }
        
        .hero-overlay::after {
            content: '';
            position: absolute;
            inset: 0;
            background-color: rgba(0, 0, 0, 0.2);
        }
        
        .hero-content {
            position: relative;
            z-index: 10;
            padding: 2.5rem;
            color: var(--white);
            text-align: center;
            max-width: 48rem;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100%;
        }
        
        .hero h2 {
            font-size: 2.25rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.2;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        @media (min-width: 768px) {
            .hero h2 {
                font-size: 3.5rem;
            }
        }
        
        .hero p {
            font-size: 1.25rem;
            margin-bottom: 2.5rem;
            opacity: 0.95;
            max-width: 40rem;
            margin-left: auto;
            margin-right: auto;
            font-weight: 300;
            text-shadow: 0 1px 5px rgba(0, 0, 0, 0.3);
        }
        
        @media (min-width: 768px) {
            .hero p {
                font-size: 1.5rem;
            }
        }
        
        .hero-btn {
            background-color: var(--accent-yellow);
            color: var(--white);
            border: none;
            padding: 1.25rem 2.5rem;
            border-radius: 0.75rem;
            font-size: 1.25rem;
            font-weight: 700;
            box-shadow: var(--shadow-xl);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin: 0 auto;
            transition: var(--transition);
            backdrop-filter: blur(4px);
            background-color: rgba(242, 169, 0, 0.95);
        }
        
        .hero-btn:hover {
            background-color: #d99700;
            box-shadow: 0 20px 25px -5px rgba(242, 169, 0, 0.4);
            transform: translateY(-4px);
        }
        
        .hero-btn:active {
            transform: scale(0.95);
        }
        
        .hero-btn svg {
            transition: var(--transition);
        }
        
        .hero-btn:hover svg {
            animation: pulse 1s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .section-title {
            color: var(--primary-blue);
            font-weight: 700;
            font-size: 2.25rem;
            margin: 2rem 0 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .section-title svg {
            background-color: #dbeafe;
            padding: 0.5rem;
            border-radius: 0.5rem;
            color: var(--accent-yellow);
        }
        
        .intro-text {
            font-size: 1.125rem;
            line-height: 1.75;
            color: var(--text-slate);
            margin-bottom: 1.5rem;
        }
        
        @media (min-width: 768px) {
            .intro-text {
                font-size: 1.25rem;
            }
        }
        
        .how-it-works {
            background-color: var(--white);
            padding: 2rem;
            border-radius: var(--border-radius-lg);
            box-shadow: var(--shadow-md);
            border: 1px solid #e2e8f0;
            transition: var(--transition);
            margin: 3rem 0;
        }
        
        .how-it-works:hover {
            box-shadow: var(--shadow-xl);
        }
        
        .how-it-works .section-title {
            text-align: center;
            margin-bottom: 2.5rem;
        }
        
        .steps {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
            margin-top: 2rem;
        }
        
        @media (min-width: 768px) {
            .steps {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        .step {
            text-align: center;
            cursor: default;
        }
        
        .step-icon {
            width: 6rem;
            height: 6rem;
            border-radius: 50%;
            background-color: #dbeafe;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            color: var(--primary-blue);
            font-size: 1.75rem;
            transition: var(--transition);
            box-shadow: var(--shadow-sm);
        }
        
        .step:hover .step-icon {
            background-color: var(--primary-blue);
            color: var(--white);
            transform: scale(1.1) rotate(3deg);
            box-shadow: var(--shadow-lg);
        }
        
        .step:nth-child(2) .step-icon:hover {
            transform: scale(1.1) rotate(-3deg);
        }
        
        .step h3 {
            font-weight: 700;
            font-size: 1.5rem;
            margin-bottom: 0.75rem;
            color: #1e293b;
            transition: var(--transition);
        }
        
        .step:hover h3 {
            color: var(--primary-blue);
        }
        
        .step p {
            font-size: 1.125rem;
            color: #475569;
        }
        
        .benefits {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        @media (min-width: 768px) {
            .benefits {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        .benefit-card {
            background-color: var(--primary-blue);
            color: var(--white);
            padding: 2rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-md);
            transition: var(--transition);
            border-top: 4px solid transparent;
        }
        
        .benefit-card:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-4px);
            border-top-color: var(--accent-yellow);
        }
        
        .benefit-card h3 {
            font-weight: 700;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid rgba(255, 255, 255, 0.3);
            padding-bottom: 0.5rem;
            display: inline-block;
        }
        
        .benefit-card p {
            opacity: 0.9;
            line-height: 1.6;
        }
        
        .services-header {
            position: relative;
            height: 16rem;
            border-radius: var(--border-radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            margin-bottom: 2rem;
        }
        
        .services-header img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.7s ease-out;
        }
        
        .services-header:hover img {
            transform: scale(1.05);
        }
        
        .services-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, 
                var(--primary-blue) 0%, 
                transparent 100%);
            opacity: 0.9;
        }
        
        .services-content {
            position: absolute;
            bottom: 0;
            left: 0;
            padding: 2rem;
            color: var(--white);
            max-width: 32rem;
        }
        
        .services-content h2 {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        @media (min-width: 768px) {
            .services-content h2 {
                font-size: 2.5rem;
            }
        }
        
        .services-content p {
            font-size: 1.25rem;
            opacity: 0.9;
            max-width: 24rem;
        }
        
        .service-cards {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        @media (min-width: 768px) {
            .service-cards {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        .service-card {
            background-color: var(--white);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-md);
            border-top: 4px solid var(--primary-blue);
            transition: var(--transition);
            cursor: default;
        }
        
        .service-card:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-8px);
        }
        
        .service-card.full-width {
            grid-column: 1 / -1;
        }
        
        .service-item {
            display: flex;
            gap: 1rem;
            align-items: flex-start;
        }
        
        .service-icon {
            background-color: #dbeafe;
            padding: 0.75rem;
            border-radius: 0.5rem;
            color: var(--primary-blue);
            flex-shrink: 0;
            transition: var(--transition);
        }
        
        .service-card:hover .service-icon {
            background-color: var(--primary-blue);
            color: var(--white);
        }
        
        .service-card:hover .service-icon svg {
            animation: pulse 1s infinite;
        }
        
        .service-card:nth-child(2) .service-icon:hover svg {
            transform: rotate(45deg);
            transition: transform 0.3s ease-out;
        }
        
        .service-card:nth-child(3) .service-icon:hover svg {
            animation: bounce 0.5s;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        
        .service-card h3 {
            font-weight: 700;
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
            color: #1e293b;
            transition: var(--transition);
        }
        
        .service-card:hover h3 {
            color: var(--primary-blue);
        }
        
        .service-card p {
            font-size: 1.125rem;
            color: #475569;
        }
        
        .warning-box {
            background-color: #fffbeb;
            border-left: 4px solid var(--accent-yellow);
            padding: 1.5rem;
            border-radius: 0 0.75rem 0.75rem 0;
            margin-top: 2rem;
            transition: var(--transition);
        }
        
        .warning-box:hover {
            background-color: #fef3c7;
        }
        
        .warning-title {
            font-weight: 700;
            font-size: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            color: #b45309;
            margin-bottom: 0.75rem;
        }
        
        .warning-title svg {
            background-color: var(--accent-yellow);
            color: var(--white);
            width: 2rem;
            height: 2rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            box-shadow: var(--shadow-sm);
            animation: pulse 2s infinite;
        }
        
        .warning-box p {
            font-size: 1.125rem;
            line-height: 1.75;
            color: #475569;
        }
        
        .schedule-header {
            margin-bottom: 2rem;
        }
        
        .schedule-header h2 {
            font-size: 2.25rem;
            font-weight: 700;
            color: var(--primary-blue);
            margin-bottom: 1rem;
        }
        
        .schedule-header p {
            font-size: 1.25rem;
            line-height: 1.75;
            color: var(--text-slate);
        }
        
        .schedule-table {
            background-color: var(--white);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-lg);
            overflow: hidden;
            border: 1px solid #e2e8f0;
            margin-bottom: 2rem;
        }
        
        table {
            width: 100%;
            min-width: 600px;
            border-collapse: collapse;
        }
        
        thead {
            background-color: var(--primary-blue);
            color: var(--white);
        }
        
        th {
            padding: 1.25rem 1.5rem;
            text-align: left;
            font-weight: 700;
            font-size: 1.25rem;
            letter-spacing: 0.025em;
        }
        
        tbody tr {
            border-bottom: 1px solid #f1f5f9;
            transition: var(--transition);
        }
        
        tbody tr:hover {
            background-color: #dbeafe;
        }
        
        tbody tr:nth-child(even) {
            background-color: #f8fafc;
        }
        
        tbody tr:nth-child(even):hover {
            background-color: #dbeafe;
        }
        
        td {
            padding: 1.5rem;
            font-size: 1.125rem;
            color: var(--text-slate);
            font-weight: 500;
        }
        
        td:first-child {
            font-weight: 700;
            color: var(--primary-blue);
        }
        
        .pdf-btn {
            background-color: var(--white);
            border: 2px solid var(--text-dark);
            color: var(--text-dark);
            padding: 0.75rem 2rem;
            border-radius: 0.75rem;
            font-size: 1.125rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 0 auto;
            cursor: pointer;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
        }
        
        .pdf-btn:hover {
            background-color: var(--text-dark);
            color: var(--white);
            transform: scale(1.05);
        }
        
        .pdf-btn:active {
            transform: scale(0.95);
        }
        
        .pdf-btn svg {
            transition: transform 0.3s ease-out;
        }
        
        .pdf-btn:hover svg {
            transform: rotate(12deg);
        }
        
        .team-header {
            position: relative;
            height: 400px;
            border-radius: var(--border-radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-xl);
            cursor: pointer;
            margin-bottom: 2rem;
        }
        
        .team-header img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.7s ease-out;
        }
        
        .team-header:hover img {
            transform: scale(1.05);
        }
        
        .team-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, 
                var(--primary-blue) 0%, 
                transparent 70%, 
                transparent 100%);
            opacity: 0.9;
        }
        
        .team-content {
            position: absolute;
            bottom: 0;
            left: 0;
            padding: 2rem;
            width: 100%;
        }
        
        .team-badge {
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            color: var(--white);
            display: inline-block;
            max-width: 32rem;
        }
        
        .team-badge h3 {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .team-badge svg {
            color: var(--accent-yellow);
            width: 2rem;
            height: 2rem;
        }
        
        .team-badge p {
            font-weight: 500;
            font-size: 1.125rem;
            opacity: 0.9;
        }
        
        .about-title {
            font-size: 2.25rem;
            font-weight: 700;
            color: var(--primary-blue);
            margin: 2rem 0 1.5rem;
        }
        
        .about-cards {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }
        
        .about-card {
            background-color: var(--white);
            padding: 2rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            border-left: 4px solid var(--accent-yellow);
            transition: var(--transition);
        }
        
        .about-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateX(8px);
        }
        
        .about-card:nth-child(2),
        .about-card:nth-child(3) {
            border-left-color: var(--primary-blue);
        }
        
        .about-card h3 {
            font-weight: 700;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--primary-blue);
        }
        
        .about-card p {
            font-size: 1.125rem;
            line-height: 1.75;
            color: var(--text-slate);
        }
        
        .contact-title {
            font-size: 2.25rem;
            font-weight: 700;
            color: var(--primary-blue);
            margin-bottom: 1rem;
        }
        
        .contact-intro {
            font-size: 1.25rem;
            line-height: 1.75;
            color: var(--text-slate);
            margin-bottom: 2rem;
        }
        
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        @media (min-width: 768px) {
            .contact-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        .phone-card {
            background: linear-gradient(to bottom right, var(--primary-blue), #003366);
            color: var(--white);
            padding: 2rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
            transition: var(--transition);
        }
        
        .phone-card:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-4px);
        }
        
        .phone-bg {
            position: absolute;
            top: 0;
            right: 0;
            padding: 2rem;
            opacity: 0.1;
            transition: var(--transition);
            transform-origin: top right;
        }
        
        .phone-card:hover .phone-bg {
            opacity: 0.2;
            transform: scale(1.25) rotate(12deg);
        }
        
        .phone-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 1rem;
            position: relative;
            z-index: 10;
        }
        
        .phone-icon {
            background-color: var(--white);
            color: var(--primary-blue);
            width: 4rem;
            height: 4rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-lg);
            transition: var(--transition);
        }
        
        .phone-card:hover .phone-icon {
            transform: scale(1.1);
        }
        
        .phone-card:hover .phone-icon svg {
            animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
        }
        
        @keyframes ping {
            75%, 100% {
                transform: scale(1.5);
                opacity: 0;
            }
        }
        
        .phone-card h3 {
            font-weight: 700;
            font-size: 1.5rem;
        }
        
        .phone-number {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            margin: 0.5rem 0;
            color: var(--accent-yellow);
            transition: var(--transition);
        }
        
        .phone-card:hover .phone-number {
            transform: scale(1.05);
        }
        
        .phone-hours {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            opacity: 0.9;
            font-size: 1.125rem;
        }
        
        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
        
        .contact-item {
            background-color: var(--white);
            padding: 1.5rem;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-md);
            border-left: 4px solid var(--accent-yellow);
            transition: var(--transition);
        }
        
        .contact-item:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-4px);
        }
        
        .contact-header {
            font-weight: 700;
            font-size: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            color: #1e293b;
            margin-bottom: 0.75rem;
        }
        
        .contact-icon {
            background-color: #dbeafe;
            padding: 0.5rem;
            border-radius: 50%;
            color: var(--primary-blue);
            transition: var(--transition);
        }
        
        .contact-item:hover .contact-icon {
            background-color: var(--accent-yellow);
            color: var(--white);
        }
        
        .contact-item a {
            font-size: 1.25rem;
            color: var(--primary-blue);
            text-decoration: underline;
            text-underline-offset: 4px;
            text-decoration-thickness: 2px;
            transition: var(--transition);
        }
        
        .contact-item a:hover {
            color: #003366;
        }
        
        .contact-item address {
            font-style: normal;
            font-size: 1.125rem;
            line-height: 1.75;
            color: var(--text-slate);
        }
        
        .map-placeholder {
            background-color: #cbd5e1;
            height: 16rem;
            border-radius: var(--border-radius);
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid #94a3b8;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }
        
        .map-placeholder:hover {
            border-color: var(--primary-blue);
        }
        
        .map-placeholder::after {
            content: '';
            position: absolute;
            inset: 0;
            background-color: rgba(148, 163, 184, 0.2);
            opacity: 0;
            transition: opacity 0.3s ease-out;
        }
        
        .map-placeholder:hover::after {
            opacity: 1;
        }
        
        .map-text {
            font-weight: 700;
            font-size: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #64748b;
            transition: var(--transition);
        }
        
        .map-placeholder:hover .map-text {
            color: var(--primary-blue);
            transform: scale(1.05);
        }
        
        /* Footer */
        footer {
            background-color: var(--text-dark);
            color: #94a3b8;
            padding: 2.5rem 0;
            margin-top: 3rem;
            border-top: 4px solid var(--accent-yellow);
        }
        
        .footer-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
        }
        
        @media (min-width: 768px) {
            .footer-content {
                flex-direction: row;
            }
        }
        
        .footer-logo {
            font-weight: 700;
            font-size: 1.125rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--white);
        }
        
        .footer-logo svg {
            color: var(--accent-yellow);
        }
        
        .footer-desc {
            opacity: 0.7;
            font-size: 0.875rem;
            margin-top: 0.5rem;
        }
        
        .footer-links {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.75rem;
            font-size: 0.875rem;
            opacity: 0.8;
        }
        
        @media (min-width: 768px) {
            .footer-links {
                flex-direction: row;
                gap: 2rem;
            }
        }
        
        .footer-link {
            color: #94a3b8;
            text-decoration: none;
            transition: var(--transition);
            cursor: pointer;
        }
        
        .footer-link:hover {
            color: var(--white);
            text-decoration: underline;
        }
        
        .footer-divider {
            display: none;
            color: #475569;
        }
        
        @media (min-width: 768px) {
            .footer-divider {
                display: inline;
            }
        }
        
        /* Responsive Navigation */
        @media (min-width: 1024px) {
            .nav-desktop {
                display: flex;
            }
            
            .mobile-menu-btn {
                display: none;
            }
        }
        
        /* Utility Classes */
        .text-center {
            text-align: center;
        }
        
        .font-bold {
            font-weight: 700;
        }
        
        .mb-4 {
            margin-bottom: 1rem;
        }
        
        .mt-8 {
            margin-top: 2rem;
        }
        
        .mb-8 {
            margin-bottom: 2rem;
        }
        
        .py-8 {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        .px-4 {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .mx-auto {
            margin-left: auto;
            margin-right: auto;
        }
        
        .hidden {
            display: none;
        }
        
        .block {
            display: block;
        }
        
        .flex {
            display: flex;
        }
        
        .items-center {
            align-items: center;
        }
        
        .justify-center {
            justify-content: center;
        }
        
        .gap-2 {
            gap: 0.5rem;
        }
        
        .gap-3 {
            gap: 0.75rem;
        }
        
        .gap-4 {
            gap: 1rem;
        }
        
        .text-xl {
            font-size: 1.25rem;
        }
        
        .text-2xl {
            font-size: 1.5rem;
        }
        
        .text-3xl {
            font-size: 1.875rem;
        }
        
        .text-4xl {
            font-size: 2.25rem;
        }
        
        .text-5xl {
            font-size: 3rem;
        }
        
        .leading-tight {
            line-height: 1.25;
        }
        
        .leading-relaxed {
            line-height: 1.625;
        }
        
        .tracking-tight {
            letter-spacing: -0.025em;
        }
        
        .tracking-wide {
            letter-spacing: 0.05em;
        }
        
        .uppercase {
            text-transform: uppercase;
        }
        
        .opacity-90 {
            opacity: 0.9;
        }
        
        .opacity-95 {
            opacity: 0.95;
        }
        
        .max-w-3xl {
            max-width: 48rem;
        }
        
        .max-w-2xl {
            max-width: 32rem;
        }
        
        .max-w-none {
            max-width: none;
        }
        
        .prose {
            max-width: 65ch;
        }
        
        .prose-xl {
            font-size: 1.25rem;
            line-height: 1.8;
        }
        
        .prose-xl p {
            margin-bottom: 1.25em;
        }
        
        .prose-xl h3 {
            margin-top: 1.5em;
            margin-bottom: 0.75em;
        }
        
        /* Icons */
        .icon {
            width: 1.25rem;
            height: 1.25rem;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        
        .icon-lg {
            width: 1.75rem;
            height: 1.75rem;
        }
        
        .icon-xl {
            width: 2.5rem;
            height: 2.5rem;
        }
    </style>
</head>
<body>
    <!-- Header / Navigation -->
    <header>
        <div class="container header-container">
            <div class="logo" id="home-link">
                <div class="logo-icon">
                    <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                    </svg>
                </div>
                <div class="logo-text">
                    <h1>Der Repair-Lieferwagen</h1>
                    <p>TFO Max Valier Projekt</p>
                </div>
            </div>
            
            <nav class="nav-desktop">
                <button class="nav-item active" data-tab="home">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path>
                    </svg>
                    Startseite
                </button>
                <button class="nav-item" data-tab="services">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                    </svg>
                    Was wir reparieren
                </button>
                <button class="nav-item" data-tab="schedule">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    Fahrplan
                </button>
                <button class="nav-item" data-tab="about">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                    Über Uns
                </button>
                <button class="nav-item" data-tab="contact">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                    </svg>
                    Kontakt
                </button>
            </nav>
            
            <button class="mobile-menu-btn" id="mobile-menu-btn">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="3" y1="12" x2="21" y2="12"></line>
                    <line x1="3" y1="6" x2="21" y2="6"></line>
                    <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
            </button>
        </div>
        
        <div class="container mobile-menu" id="mobile-menu">
            <nav>
                <button class="mobile-nav-item active" data-tab="home">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path>
                    </svg>
                    Startseite
                </button>
                <button class="mobile-nav-item" data-tab="services">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                    </svg>
                    Was wir reparieren
                </button>
                <button class="mobile-nav-item" data-tab="schedule">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    Fahrplan
                </button>
                <button class="mobile-nav-item" data-tab="about">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                    Über Uns
                </button>
                <button class="mobile-nav-item" data-tab="contact">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                    </svg>
                    Kontakt
                </button>
            </nav>
        </div>
    </header>
    
    <!-- Main Content -->
    <main class="container">
        <!-- HOME VIEW -->
        <div class="view active" id="home-view">
            <div class="hero">
                <img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=2021&auto=format&fit=crop" alt="Repair Van in den Bergen" class="hero-img">
                <div class="hero-overlay"></div>
                <div class="hero-content">
                    <h2>Wir bringen Hilfe <br>in Ihr Dorf.</h2>
                    <p>Kostenlose Reparaturen, technische Unterstützung und ein offenes Ohr – <span style="font-weight:600;color:var(--accent-yellow)">von Schülern für Senioren.</span></p>
                    <button class="hero-btn" id="schedule-btn">
                        <svg class="icon-lg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="16" y1="2" x2="16" y2="6"></line>
                            <line x1="8" y1="2" x2="8" y2="6"></line>
                            <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                        Wann kommen wir zu Ihnen?
                    </button>
                </div>
            </div>
            
            <section class="prose prose-xl max-w-none text-slate-700 mt-8">
                <h3 class="section-title">
                    <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path>
                    </svg>
                    Willkommen beim Repair-Lieferwagen!
                </h3>
                <p class="intro-text">
                    Manchmal sind es die kleinen Dinge, die im Alltag Sorgen bereiten: Der Toaster streikt, das Radio bleibt stumm oder der Föhn funktioniert nicht mehr. Oft fehlt nur ein geschickter Handgriff, um diese Dinge wieder zum Laufen zu bringen.
                </p>
                <p class="intro-text">
                    Genau dafür sind wir da. Unsere Schülerinnen und Schüler kommen mit dem Werkstatt-Bus direkt in Ihre Gemeinde. Wir reparieren Ihre Alltagsgegenstände und nehmen uns Zeit für ein gutes Gespräch.
                </p>
            </section>
            
            <section class="how-it-works">
                <h3 class="section-title text-center">So funktioniert es</h3>
                <div class="steps">
                    <div class="step">
                        <div class="step-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                        </div>
                        <h3>1. Fahrplan prüfen</h3>
                        <p>Schauen Sie nach, wann unser Bus in Ihrem Dorf hält.</p>
                    </div>
                    <div class="step">
                        <div class="step-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                                <circle cx="12" cy="10" r="3"></circle>
                            </svg>
                        </div>
                        <h3>2. Vorbeikommen</h3>
                        <p>Bringen Sie Ihr defektes Gerät einfach zum Standplatz. Keine Anmeldung nötig.</p>
                    </div>
                    <div class="step">
                        <div class="step-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                <circle cx="9" cy="7" r="4"></circle>
                                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                            </svg>
                        </div>
                        <h3>3. Reparatur & Austausch</h3>
                        <p>Während wir reparieren, laden wir Sie ein, uns kennenzulernen.</p>
                    </div>
                </div>
            </section>
            
            <div class="benefits">
                <div class="benefit-card">
                    <h3>Kostenlos</h3>
                    <p>Unser Service ist für Seniorinnen und Senioren gratis.</p>
                </div>
                <div class="benefit-card">
                    <h3>Nachhaltig</h3>
                    <p>Reparieren statt Wegwerfen schont die Umwelt.</p>
                </div>
                <div class="benefit-card">
                    <h3>Gemeinsam</h3>
                    <p>Wir lernen von Ihrer Lebenserfahrung, Sie profitieren von unserem Fachwissen.</p>
                </div>
            </div>
        </div>
        
        <!-- SERVICES VIEW -->
        <div class="view" id="services-view">
            <div class="services-header">
                <img src="https://images.unsplash.com/photo-1581092921461-eab62e97a780?q=80&w=2070&auto=format&fit=crop" alt="Reparaturarbeiten">
                <div class="services-overlay"></div>
                <div class="services-content">
                    <h2>Was können wir für Sie tun?</h2>
                    <p>Da wir Schüler einer technischen Schule sind, decken wir alle Bereiche ab, die wir auch im Unterricht lernen.</p>
                </div>
            </div>
            
            <div class="service-cards">
                <div class="service-card">
                    <div class="service-item">
                        <div class="service-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M8 18v-6M16 18v-6M8.5 6.5h7M21 16v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1M3 3h18v4H3V3z"></path>
                            </svg>
                        </div>
                        <div>
                            <h3>Elektrische Kleingeräte</h3>
                            <p>Wir überprüfen und reparieren Küchengeräte (Mixer, Toaster, Kaffeemühlen), Föhne, alte Radios, Lampen und mehr.</p>
                        </div>
                    </div>
                </div>
                
                <div class="service-card">
                    <div class="service-item">
                        <div class="service-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                            </svg>
                        </div>
                        <div>
                            <h3>Mechanische Gegenstände</h3>
                            <p>Wackelige Stühle, klemmende Schubladen oder einfaches Spielzeug und mechanische Uhren.</p>
                        </div>
                    </div>
                </div>
                
                <div class="service-card full-width">
                    <div class="service-item">
                        <div class="service-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                            </svg>
                        </div>
                        <div>
                            <h3>Hilfe bei Technikfragen</h3>
                            <p>Haben Sie Fragen zur Bedienung eines Geräts? Wir erklären es Ihnen gerne in Ruhe.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="warning-box">
                <div class="warning-title">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="8" x2="12" y2="12"></line>
                        <line x1="12" y1="16" x2="12.01" y2="16"></line>
                    </svg>
                    Wichtiger Hinweis
                </div>
                <p>
                    Bitte beachten Sie: Großgeräte wie Waschmaschinen oder Kühlschränke können wir im Bus leider nicht reparieren. Auch übernehmen wir keine Garantie wie ein gewerblicher Betrieb – wir geben aber unser Bestes, mit Sorgfalt und Fachwissen zu helfen. Die notwendigen Ersatzteile müssen gegebenenfalls besorgt werden.
                </p>
            </div>
        </div>
        
        <!-- SCHEDULE VIEW -->
        <div class="view" id="schedule-view">
            <div class="schedule-header">
                <h2 class="contact-title">Wann sind wir in Ihrer Nähe?</h2>
                <p class="contact-intro">
                    Hier finden Sie die nächsten Termine. Wir stehen meist auf dem Hauptplatz oder in der Nähe des Gemeindehauses, gut sichtbar mit unserem Repair-Lieferwagen.
                </p>
            </div>
            
            <div class="schedule-table">
                <table>
                    <thead>
                        <tr>
                            <th>Datum</th>
                            <th>Uhrzeit</th>
                            <th>Gemeinde</th>
                            <th>Standort</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Mo, 12. Mai</td>
                            <td>09:00 – 12:00</td>
                            <td>Eppan</td>
                            <td>Rathausplatz</td>
                        </tr>
                        <tr>
                            <td>Mi, 14. Mai</td>
                            <td>14:00 – 17:00</td>
                            <td>Kaltern</td>
                            <td>Marktplatz</td>
                        </tr>
                        <tr>
                            <td>Fr, 16. Mai</td>
                            <td>09:00 – 12:00</td>
                            <td>Sarnthein</td>
                            <td>Kirchplatz</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="text-center pt-4">
                <button class="pdf-btn">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 20h9"></path>
                        <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                    </svg>
                    Plan als PDF herunterladen
                </button>
            </div>
        </div>
        
        <!-- ABOUT VIEW -->
        <div class="view" id="about-view">
            <div class="team-header">
                <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop" alt="Klasse 4Log A">
                <div class="team-overlay"></div>
                <div class="team-content">
                    <div class="team-badge">
                        <h3>
                            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="2"></circle>
                                <path d="M16 8.5L12 4 8 8.5"></path>
                                <path d="M11 14h2"></path>
                                <path d="M12 11v3"></path>
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            </svg>
                            Klasse 4Log A
                        </h3>
                        <p>Die Schülerinnen und Schüler der TFO Max Valier bereit für den Einsatz.</p>
                    </div>
                </div>
            </div>
            
            <h2 class="about-title">Jung und Alt – Hand in Hand.</h2>
            
            <div class="about-cards">
                <div class="about-card">
                    <h3>Die Mission</h3>
                    <p>
                        Der Repair-Lieferwagen ist mehr als nur eine fahrbare Werkstatt. Er ist ein Projekt unserer Schule, um Brücken zu bauen. Wir möchten nicht nur im Klassenzimmer lernen, sondern unser Wissen dort einsetzen, wo es gebraucht wird: bei den Menschen in unseren Südtiroler Dörfern.
                    </p>
                </div>
                
                <div class="about-card">
                    <h3>Unsere Motivation</h3>
                    <p>
                        Für uns junge Menschen ist dies eine wertvolle Gelegenheit. Wir lernen, Verantwortung zu übernehmen, technische Probleme in der Praxis zu lösen und – was uns besonders wichtig ist – wir hören zu. Der Austausch mit der älteren Generation ist für uns eine Bereicherung.
                    </p>
                </div>
                
                <div class="about-card">
                    <h3>Das Team</h3>
                    <p>
                        Wir sind die Schülerinnen und Schüler der Klasse 4Log A der TFO Max Valier. Begleitet werden wir von unseren Fachlehrern, die uns bei kniffligen Fällen unterstützen.
                    </p>
                </div>
            </div>
        </div>
        
        <!-- CONTACT VIEW -->
        <div class="view" id="contact-view">
            <h2 class="contact-title">Haben Sie noch Fragen?</h2>
            <p class="contact-intro">
                Sind Sie unsicher, ob wir Ihr Gerät reparieren können? Oder möchten Sie wissen, ob der Bus auch in Ihr Dorf kommt? Rufen Sie uns gerne an.
            </p>
            
            <div class="contact-grid">
                <div class="phone-card">
                    <div class="phone-bg">
                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                        </svg>
                    </div>
                    <div class="phone-content">
                        <div class="phone-icon">
                            <svg class="icon-xl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                            </svg>
                        </div>
                        <h3>Rufen Sie uns an</h3>
                        <div class="phone-number">+39 0471 123 456</div>
                        <div class="phone-hours">
                            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14"></polyline>
                            </svg>
                            Mo–Fr von 08:00 bis 12:00 Uhr
                        </div>
                    </div>
                </div>
                
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-header">
                            <div class="contact-icon">
                                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="9" cy="7" r="4"></circle>
                                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                                </svg>
                            </div>
                            E-Mail
                        </div>
                        <a href="mailto:info@repair-lieferwagen.it">info@repair-lieferwagen.it</a>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-header">
                            <div class="contact-icon">
                                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                                    <circle cx="12" cy="10" r="3"></circle>
                                </svg>
                            </div>
                            Unser Standort
                        </div>
                        <address>
                            TFO Max Valier<br>
                            Sorrentostraße 20<br>
                            39100 Bozen
                        </address>
                    </div>
                </div>
            </div>
            
            <div class="map-placeholder">
                <div class="map-text">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                    </svg>
                    Karte der Schule
                </div>
            </div>
        </div>
    </main>
    
    <!-- Footer -->
    <footer>
        <div class="container footer-content">
            <div>
                <div class="footer-logo">
                    <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                    </svg>
                    Der Repair-Lieferwagen
                </div>
                <p class="footer-desc">Ein Schulprojekt der TFO Max Valier für Südtirol.</p>
            </div>
            <div class="footer-links">
                <span class="footer-link" id="footer-contact">Kontakt</span>
                <span class="footer-divider">|</span>
                <span class="footer-link">Impressum</span>
                <span class="footer-divider">|</span>
                <span class="footer-link">Datenschutz</span>
            </div>
        </div>
    </footer>
    
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Navigation elements
            const navItems = document.querySelectorAll('[data-tab]');
            const views = document.querySelectorAll('.view');
            const mobileMenuBtn = document.getElementById('mobile-menu-btn');
            const mobileMenu = document.getElementById('mobile-menu');
            const homeLink = document.getElementById('home-link');
            const scheduleBtn = document.getElementById('schedule-btn');
            const footerContact = document.getElementById('footer-contact');
            
            // Close mobile menu function
            const closeMobileMenu = () => {
                mobileMenu.classList.remove('active');
            };
            
            // Navigation function
            const navigateTo = (tabId) => {
                // Update active nav items
                navItems.forEach(item => {
                    if (item.dataset.tab === tabId) {
                        item.classList.add('active');
                    } else {
                        item.classList.remove('active');
                    }
                });
                
                // Show active view
                views.forEach(view => {
                    if (view.id === `${tabId}-view`) {
                        view.classList.add('active');
                    } else {
                        view.classList.remove('active');
                    }
                });
                
                // Close mobile menu if open
                closeMobileMenu();
                
                // Scroll to top
                window.scrollTo(0, 0);
            };
            
            // Set up navigation event listeners
            navItems.forEach(item => {
                item.addEventListener('click', () => {
                    navigateTo(item.dataset.tab);
                });
            });
            
            // Mobile menu toggle
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('active');
            });
            
            // Home logo click
            homeLink.addEventListener('click', () => {
                navigateTo('home');
            });
            
            // Schedule button in hero section
            scheduleBtn.addEventListener('click', () => {
                navigateTo('schedule');
            });
            
            // Footer contact link
            footerContact.addEventListener('click', () => {
                navigateTo('contact');
            });
            
            // Initialize with home view active
            navigateTo('home');
        });
    </script>
</body>
</html>

