import http.server
import socketserver

# The complete HTML for the home page
HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SRS MECHATRONICS INSTRUMENTATIONS | Testing Excellence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        /* Custom styles for smooth scrolling and animations */
        html { scroll-behavior: smooth; }
        .hero-pattern {
            background-color: #0f172a;
            background-image: radial-gradient(#1e293b 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .fade-in { animation: fadeIn 1.5s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

    <!-- Navigation Bar -->
    <nav class="bg-white shadow-md fixed w-full z-50 top-0">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex items-center gap-2">
                        <i data-lucide="cpu" class="h-8 w-8 text-blue-700"></i>
                        <span class="font-bold text-xl tracking-tight text-blue-900 leading-tight">
                            SRS MECHATRONICS<br><span class="text-sm font-medium text-gray-500">INSTRUMENTATIONS</span>
                        </span>
                    </div>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Home</a>
                    <a href="/about" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">About Us</a>
                    <div class="relative">
                        <button class="text-gray-700 hover:text-blue-700 font-medium transition-colors flex items-center gap-1" onclick="toggleDropdown()">
                            Products <i data-lucide="chevron-down" class="h-4 w-4"></i>
                        </button>
                        <div id="products-dropdown" class="absolute top-full left-0 mt-2 w-64 bg-white rounded-md shadow-lg border border-gray-200 opacity-0 invisible transform translate-y-2 transition-all duration-200 z-50">
                            <div class="py-2">
                                <a href="/products#chemical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flask-conical" class="h-4 w-4 inline mr-2"></i>Chemical Tests
                                </a>
                                <a href="/products#electrical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="zap" class="h-4 w-4 inline mr-2"></i>Electrical Tests
                                </a>
                                <a href="/products#environmental" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="thermometer" class="h-4 w-4 inline mr-2"></i>Environmental Tests
                                </a>
                                <a href="/products#fire-smoke" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flame" class="h-4 w-4 inline mr-2"></i>Fire and Smoke Tests
                                </a>
                                <a href="/products#optical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="eye" class="h-4 w-4 inline mr-2"></i>Optical Tests
                                </a>
                                <a href="/products#sample-prep" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="test-tube" class="h-4 w-4 inline mr-2"></i>Sample Preparation
                                </a>
                            </div>
                        </div>
                    </div>
                    <a href="/services" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Services</a>
                    <a href="/contact" class="bg-blue-700 text-white px-5 py-2 rounded-md hover:bg-blue-800 transition-colors font-medium">Contact Us</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-pattern pt-32 pb-20 md:pt-40 md:pb-28 text-white min-h-[80vh] flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 fade-in">
            <div class="max-w-3xl">
                <div class="inline-block bg-blue-600/20 text-blue-300 font-semibold px-4 py-1 rounded-full mb-6 border border-blue-500/30">
                    The New Benchmark in Testing
                </div>
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight">
                    Engineering Expertise.<br>
                    <span class="text-blue-500">Global Reliability.</span>
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 leading-relaxed">
                    Trusted experts in manufacturing standard compliant test instruments. We innovate, design, and develop precision equipment for analytical and industrial applications worldwide.
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="#products" class="bg-blue-600 text-white text-center px-8 py-4 rounded-md font-bold hover:bg-blue-700 transition-colors">
                        Explore Our Products
                    </a>
                    <a href="#contact" class="bg-transparent border-2 border-white text-white text-center px-8 py-4 rounded-md font-bold hover:bg-white hover:text-slate-900 transition-colors">
                        Get a Quote
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Bar -->
    <section class="bg-blue-800 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
                <div>
                    <i data-lucide="award" class="h-10 w-10 mx-auto mb-4 text-blue-300"></i>
                    <h3 class="text-3xl font-bold mb-2">40+</h3>
                    <p class="text-blue-200">Years Engineering Expertise</p>
                </div>
                <div>
                    <i data-lucide="globe-2" class="h-10 w-10 mx-auto mb-4 text-blue-300"></i>
                    <h3 class="text-3xl font-bold mb-2">60+</h3>
                    <p class="text-blue-200">Countries Exporting</p>
                </div>
                <div>
                    <i data-lucide="users" class="h-10 w-10 mx-auto mb-4 text-blue-300"></i>
                    <h3 class="text-3xl font-bold mb-2">1000+</h3>
                    <p class="text-blue-200">Satisfied Customers</p>
                </div>
                <div>
                    <i data-lucide="check-circle-2" class="h-10 w-10 mx-auto mb-4 text-blue-300"></i>
                    <h3 class="text-3xl font-bold mb-2">100%</h3>
                    <p class="text-blue-200">Test Standard Compliance</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="py-20 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Our Core Products & Categories</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
                <p class="text-gray-600 max-w-2xl mx-auto">Reliable, robust, and easy-to-use test instrumentation designed specifically for the cable, textile, plastics, and mechatronics industries.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Product Card 1 -->
                <div class="bg-white rounded-xl shadow-sm hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gray-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="flame" class="h-16 w-16 text-gray-400 group-hover:text-blue-500 transition-colors"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-2">Fire & Smoke Tests</h3>
                        <p class="text-gray-600 mb-4">Evaluate fire behavior with Heat Release Rates, Oxygen Index, and Total Smoke Production measuring units.</p>
                        <a href="#" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Know More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Product Card 2 -->
                <div class="bg-white rounded-xl shadow-sm hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gray-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="activity" class="h-16 w-16 text-gray-400 group-hover:text-blue-500 transition-colors"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-2">Physical & Mechanical Tests</h3>
                        <p class="text-gray-600 mb-4">Comprehensive solutions for testing tensile strength, abrasion resistance, and mechanical endurance.</p>
                        <a href="#" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Know More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Product Card 3 -->
                <div class="bg-white rounded-xl shadow-sm hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gray-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="thermometer-snowflake" class="h-16 w-16 text-gray-400 group-hover:text-blue-500 transition-colors"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-2">Climatic & Low Temp Chambers</h3>
                        <p class="text-gray-600 mb-4">Provide extra reliability during stability testing and simulate extreme environmental conditions flawlessly.</p>
                        <a href="#" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Know More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us / Quality Assurance -->
    <section id="quality" class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row items-center gap-12">
                <div class="md:w-1/2">
                    <h2 class="text-3xl font-bold text-gray-900 mb-4">Why Choose SRS Mechatronics?</h2>
                    <div class="h-1 w-20 bg-blue-600 mb-8"></div>
                    <p class="text-gray-600 mb-6 text-lg">
                        Originally established with an outlook to manufacture instruments for analytical and industrial applications, we have expanded our manufacturing processes to innovate, design and develop instruments specific to complex engineering demands.
                    </p>
                    <ul class="space-y-4">
                        <li class="flex items-start">
                            <i data-lucide="check-circle" class="h-6 w-6 text-blue-600 mt-1 mr-3 flex-shrink-0"></i>
                            <div>
                                <h4 class="font-bold text-gray-900">Engineering Expertise</h4>
                                <p class="text-gray-600 text-sm">Trusted brand in manufacturing standard-compliant test instruments.</p>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <i data-lucide="shield-check" class="h-6 w-6 text-blue-600 mt-1 mr-3 flex-shrink-0"></i>
                            <div>
                                <h4 class="font-bold text-gray-900">Trust and Confidentiality</h4>
                                <p class="text-gray-600 text-sm">We understand the importance of trust and intellectual property in modern industry.</p>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <i data-lucide="microscope" class="h-6 w-6 text-blue-600 mt-1 mr-3 flex-shrink-0"></i>
                            <div>
                                <h4 class="font-bold text-gray-900">Quality Assurance</h4>
                                <p class="text-gray-600 text-sm">Delivering test instruments with the latest technology and relentless innovation.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="md:w-1/2 w-full">
                    <div class="bg-gray-100 rounded-2xl p-8 border border-gray-200">
                        <div class="grid grid-cols-2 gap-4">
                            <div class="bg-white p-4 rounded-xl shadow-sm text-center border-t-4 border-blue-600">
                                <i data-lucide="zap" class="h-8 w-8 text-blue-600 mx-auto mb-2"></i>
                                <h5 class="font-bold text-gray-800">Electrical Tests</h5>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-sm text-center border-t-4 border-blue-600">
                                <i data-lucide="beaker" class="h-8 w-8 text-blue-600 mx-auto mb-2"></i>
                                <h5 class="font-bold text-gray-800">Chemical Tests</h5>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-sm text-center border-t-4 border-blue-600">
                                <i data-lucide="eye" class="h-8 w-8 text-blue-600 mx-auto mb-2"></i>
                                <h5 class="font-bold text-gray-800">Optical Tests</h5>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-sm text-center border-t-4 border-blue-600">
                                <i data-lucide="layers" class="h-8 w-8 text-blue-600 mx-auto mb-2"></i>
                                <h5 class="font-bold text-gray-800">Sample Prep</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Form Section -->
    <section id="contact" class="py-20 bg-gray-50 border-t border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Let's Build the Future Together</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
                <p class="text-gray-600">Reach out to our engineering experts for inquiries, quotes, or support.</p>
            </div>
            
            <div class="max-w-3xl mx-auto bg-white rounded-xl shadow-md p-8">
                <form class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Name *</label>
                            <input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" required>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
                            <input type="email" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" required>
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
                        <input type="tel" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Message *</label>
                        <textarea rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" required></textarea>
                    </div>
                    <button type="button" onclick="alert('Message Sent Successfully! (Demo Only)')" class="w-full bg-blue-700 text-white font-bold py-3 px-4 rounded-md hover:bg-blue-800 transition-colors">
                        Send Message
                    </button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-gray-300 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div class="col-span-1 md:col-span-2">
                    <div class="flex items-center gap-2 mb-4">
                        <i data-lucide="cpu" class="h-6 w-6 text-blue-500"></i>
                        <span class="font-bold text-lg text-white">SRS MECHATRONICS</span>
                    </div>
                    <p class="text-sm text-gray-400 max-w-sm mb-4">
                        Trusted name in quality test instruments. We manufacture standard-compliant test equipment with excellent reliability and performance globally.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="linkedin" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="twitter" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="mail" class="h-5 w-5"></i></a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-white font-bold mb-4">Our Products</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="#" class="hover:text-blue-400 transition-colors">Fire & Smoke Tests</a></li>
                        <li><a href="#" class="hover:text-blue-400 transition-colors">Physical & Mechanical Tests</a></li>
                        <li><a href="#" class="hover:text-blue-400 transition-colors">Environmental Chambers</a></li>
                        <li><a href="#" class="hover:text-blue-400 transition-colors">Optical & Chemical Tests</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold mb-4">Contact Info</h4>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <i data-lucide="map-pin" class="h-4 w-4 mr-2 mt-0.5 text-blue-500 flex-shrink-0"></i>
                            <span>Delhi, India</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="phone" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>+91 XXXXX XXXXX</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="mail" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>info@srsmechatronics.com</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 text-center text-sm text-gray-500">
                <p>&copy; 2026 SRS Mechatronics Instrumentations. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Initialize Icons -->
    <script>
        function toggleDropdown() {
            const dropdown = document.getElementById('products-dropdown');
            const isVisible = dropdown.classList.contains('opacity-100');
            
            if (isVisible) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            } else {
                dropdown.classList.remove('opacity-0', 'invisible');
                dropdown.classList.add('opacity-100', 'visible');
            }
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const dropdown = document.getElementById('products-dropdown');
            const button = event.target.closest('button');
            
            if (!button || !button.onclick || button.onclick.toString().indexOf('toggleDropdown') === -1) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            }
        });

        lucide.createIcons();
    </script>
</body>
</html>
"""

ABOUT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - SRS MECHATRONICS INSTRUMENTATIONS</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .hero-pattern {
            background-color: #0f172a;
            background-image: radial-gradient(#1e293b 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .fade-in { animation: fadeIn 1.5s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

    <!-- Navigation Bar -->
    <nav class="bg-white shadow-md fixed w-full z-50 top-0">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex items-center gap-2">
                        <i data-lucide="cpu" class="h-8 w-8 text-blue-700"></i>
                        <span class="font-bold text-xl tracking-tight text-blue-900 leading-tight">
                            SRS MECHATRONICS<br><span class="text-sm font-medium text-gray-500">INSTRUMENTATIONS</span>
                        </span>
                    </div>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Home</a>
                    <a href="/about" class="text-blue-700 font-medium transition-colors">About Us</a>
                    <div class="relative">
                        <button class="text-gray-700 hover:text-blue-700 font-medium transition-colors flex items-center gap-1" onclick="toggleDropdown()">
                            Products <i data-lucide="chevron-down" class="h-4 w-4"></i>
                        </button>
                        <div id="products-dropdown" class="absolute top-full left-0 mt-2 w-64 bg-white rounded-md shadow-lg border border-gray-200 opacity-0 invisible transform translate-y-2 transition-all duration-200 z-50">
                            <div class="py-2">
                                <a href="/products#chemical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flask-conical" class="h-4 w-4 inline mr-2"></i>Chemical Tests
                                </a>
                                <a href="/products#electrical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="zap" class="h-4 w-4 inline mr-2"></i>Electrical Tests
                                </a>
                                <a href="/products#environmental" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="thermometer" class="h-4 w-4 inline mr-2"></i>Environmental Tests
                                </a>
                                <a href="/products#fire-smoke" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flame" class="h-4 w-4 inline mr-2"></i>Fire and Smoke Tests
                                </a>
                                <a href="/products#optical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="eye" class="h-4 w-4 inline mr-2"></i>Optical Tests
                                </a>
                                <a href="/products#sample-prep" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="test-tube" class="h-4 w-4 inline mr-2"></i>Sample Preparation
                                </a>
                            </div>
                        </div>
                    </div>
                    <a href="/services" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Services</a>
                    <a href="/contact" class="bg-blue-700 text-white px-5 py-2 rounded-md hover:bg-blue-800 transition-colors font-medium">Contact Us</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-pattern pt-32 pb-20 text-white min-h-[60vh] flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 fade-in">
            <div class="max-w-4xl">
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight">
                    About SRS Mechatronics
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 leading-relaxed">
                    Pioneering precision testing solutions for over 40 years. We combine engineering expertise with cutting-edge technology to deliver reliable test instruments worldwide.
                </p>
            </div>
        </div>
    </section>

    <!-- Our Story Section -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-3xl font-bold text-gray-900 mb-6">Our Story</h2>
                    <p class="text-gray-600 mb-6">
                        Founded in 1986, SRS Mechatronics Instrumentations began with a vision to revolutionize testing equipment for analytical and industrial applications. What started as a small workshop has grown into a global leader in precision instrumentation.
                    </p>
                    <p class="text-gray-600 mb-6">
                        Our journey has been driven by relentless innovation and an unwavering commitment to quality. We've expanded our capabilities to meet the complex demands of modern engineering, from fire safety testing to environmental simulation.
                    </p>
                    <div class="flex items-center gap-4">
                        <div class="bg-blue-100 p-3 rounded-full">
                            <i data-lucide="award" class="h-6 w-6 text-blue-600"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-gray-900">40+ Years of Excellence</h4>
                            <p class="text-gray-600 text-sm">Trusted by industry leaders worldwide</p>
                        </div>
                    </div>
                </div>
                <div class="bg-gray-100 rounded-2xl p-8">
                    <div class="grid grid-cols-2 gap-6">
                        <div class="text-center">
                            <div class="text-4xl font-bold text-blue-600 mb-2">1986</div>
                            <p class="text-gray-600">Founded</p>
                        </div>
                        <div class="text-center">
                            <div class="text-4xl font-bold text-blue-600 mb-2">60+</div>
                            <p class="text-gray-600">Countries</p>
                        </div>
                        <div class="text-center">
                            <div class="text-4xl font-bold text-blue-600 mb-2">1000+</div>
                            <p class="text-gray-600">Customers</p>
                        </div>
                        <div class="text-center">
                            <div class="text-4xl font-bold text-blue-600 mb-2">50+</div>
                            <p class="text-gray-600">Products</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Mission & Vision -->
    <section class="py-20 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Our Mission & Vision</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                <div class="bg-white p-8 rounded-xl shadow-sm">
                    <div class="flex items-center mb-6">
                        <div class="bg-blue-100 p-3 rounded-full mr-4">
                            <i data-lucide="target" class="h-8 w-8 text-blue-600"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-gray-900">Our Mission</h3>
                    </div>
                    <p class="text-gray-600">
                        To provide innovative, reliable, and precise testing instruments that enable our customers to achieve the highest standards of quality and safety in their products and processes.
                    </p>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-sm">
                    <div class="flex items-center mb-6">
                        <div class="bg-blue-100 p-3 rounded-full mr-4">
                            <i data-lucide="eye" class="h-8 w-8 text-blue-600"></i>
                        </div>
                        <h3 class="text-2xl font-bold text-gray-900">Our Vision</h3>
                    </div>
                    <p class="text-gray-600">
                        To be the global leader in testing instrumentation, recognized for our engineering excellence, customer-centric approach, and commitment to advancing industrial standards.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Meet Our Leadership Team</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
                <p class="text-gray-600 max-w-2xl mx-auto">Experienced professionals dedicated to driving innovation and excellence in testing technology.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                        <i data-lucide="user" class="h-16 w-16 text-gray-400"></i>
                    </div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Dr. Rajesh Kumar</h4>
                    <p class="text-blue-600 font-medium mb-2">CEO & Founder</p>
                    <p class="text-gray-600 text-sm">40+ years in materials testing and instrumentation design.</p>
                </div>
                <div class="text-center">
                    <div class="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                        <i data-lucide="user" class="h-16 w-16 text-gray-400"></i>
                    </div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Priya Sharma</h4>
                    <p class="text-blue-600 font-medium mb-2">Chief Technology Officer</p>
                    <p class="text-gray-600 text-sm">Leading innovation in smart testing solutions and IoT integration.</p>
                </div>
                <div class="text-center">
                    <div class="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                        <i data-lucide="user" class="h-16 w-16 text-gray-400"></i>
                    </div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Amit Patel</h4>
                    <p class="text-blue-600 font-medium mb-2">Head of Engineering</p>
                    <p class="text-gray-600 text-sm">Expert in mechanical design and precision manufacturing.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-gray-300 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div class="col-span-1 md:col-span-2">
                    <div class="flex items-center gap-2 mb-4">
                        <i data-lucide="cpu" class="h-6 w-6 text-blue-500"></i>
                        <span class="font-bold text-lg text-white">SRS MECHATRONICS</span>
                    </div>
                    <p class="text-sm text-gray-400 max-w-sm mb-4">
                        Trusted name in quality test instruments. We manufacture standard-compliant test equipment with excellent reliability and performance globally.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="linkedin" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="twitter" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="mail" class="h-5 w-5"></i></a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-white font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/" class="hover:text-blue-400 transition-colors">Home</a></li>
                        <li><a href="/about" class="hover:text-blue-400 transition-colors">About Us</a></li>
                        <li><a href="/products" class="hover:text-blue-400 transition-colors">Products</a></li>
                        <li><a href="/services" class="hover:text-blue-400 transition-colors">Services</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold mb-4">Contact Info</h4>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <i data-lucide="map-pin" class="h-4 w-4 mr-2 mt-0.5 text-blue-500 flex-shrink-0"></i>
                            <span>Delhi, India</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="phone" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>+91 XXXXX XXXXX</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="mail" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>info@srsmechatronics.com</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 text-center text-sm text-gray-500">
                <p>&copy; 2026 SRS Mechatronics Instrumentations. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleDropdown() {
            const dropdown = document.getElementById('products-dropdown');
            const isVisible = dropdown.classList.contains('opacity-100');
            
            if (isVisible) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            } else {
                dropdown.classList.remove('opacity-0', 'invisible');
                dropdown.classList.add('opacity-100', 'visible');
            }
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const dropdown = document.getElementById('products-dropdown');
            const button = event.target.closest('button');
            
            if (!button || !button.onclick || button.onclick.toString().indexOf('toggleDropdown') === -1) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            }
        });

        lucide.createIcons();
    </script>
</body>
</html>
"""

PRODUCTS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products - SRS MECHATRONICS INSTRUMENTATIONS</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .hero-pattern {
            background-color: #0f172a;
            background-image: radial-gradient(#1e293b 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .fade-in { animation: fadeIn 1.5s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

    <!-- Navigation Bar -->
    <nav class="bg-white shadow-md fixed w-full z-50 top-0">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex items-center gap-2">
                        <i data-lucide="cpu" class="h-8 w-8 text-blue-700"></i>
                        <span class="font-bold text-xl tracking-tight text-blue-900 leading-tight">
                            SRS MECHATRONICS<br><span class="text-sm font-medium text-gray-500">INSTRUMENTATIONS</span>
                        </span>
                    </div>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Home</a>
                    <a href="/about" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">About Us</a>
                    <div class="relative">
                        <button class="text-blue-700 font-medium transition-colors flex items-center gap-1" onclick="toggleDropdown()">
                            Products <i data-lucide="chevron-down" class="h-4 w-4"></i>
                        </button>
                        <div id="products-dropdown" class="absolute top-full left-0 mt-2 w-64 bg-white rounded-md shadow-lg border border-gray-200 opacity-0 invisible transform translate-y-2 transition-all duration-200 z-50">
                            <div class="py-2">
                                <a href="/products#chemical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flask-conical" class="h-4 w-4 inline mr-2"></i>Chemical Tests
                                </a>
                                <a href="/products#electrical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="zap" class="h-4 w-4 inline mr-2"></i>Electrical Tests
                                </a>
                                <a href="/products#environmental" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="thermometer" class="h-4 w-4 inline mr-2"></i>Environmental Tests
                                </a>
                                <a href="/products#fire-smoke" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flame" class="h-4 w-4 inline mr-2"></i>Fire and Smoke Tests
                                </a>
                                <a href="/products#optical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="eye" class="h-4 w-4 inline mr-2"></i>Optical Tests
                                </a>
                                <a href="/products#sample-prep" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="test-tube" class="h-4 w-4 inline mr-2"></i>Sample Preparation
                                </a>
                            </div>
                        </div>
                    </div>
                    <a href="/services" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Services</a>
                    <a href="/contact" class="bg-blue-700 text-white px-5 py-2 rounded-md hover:bg-blue-800 transition-colors font-medium">Contact Us</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-pattern pt-32 pb-20 text-white min-h-[50vh] flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 fade-in">
            <div class="max-w-4xl">
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight">
                    Our Products
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 leading-relaxed">
                    Comprehensive range of precision testing instruments designed for reliability, accuracy, and compliance with international standards.
                </p>
            </div>
        </div>
    </section>

    <!-- Product Categories -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Product Categories</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
                <p class="text-gray-600 max-w-2xl mx-auto">Explore our comprehensive range of testing solutions across multiple categories.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Fire & Smoke Tests -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gradient-to-br from-red-100 to-red-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="flame" class="h-20 w-20 text-red-500 group-hover:scale-110 transition-transform"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-3">Fire & Smoke Tests</h3>
                        <p class="text-gray-600 mb-4">Advanced equipment for evaluating fire behavior, heat release rates, oxygen index, and smoke production measurements.</p>
                        <ul class="text-sm text-gray-600 mb-4 space-y-1">
                            <li>• Cone Calorimeter</li>
                            <li>• Smoke Density Chamber</li>
                            <li>• Oxygen Index Tester</li>
                            <li>• Heat Release Rate Apparatus</li>
                        </ul>
                        <a href="#fire-details" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Learn More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Physical & Mechanical Tests -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gradient-to-br from-blue-100 to-blue-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="activity" class="h-20 w-20 text-blue-500 group-hover:scale-110 transition-transform"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-3">Physical & Mechanical Tests</h3>
                        <p class="text-gray-600 mb-4">Comprehensive solutions for testing tensile strength, abrasion resistance, impact resistance, and mechanical endurance.</p>
                        <ul class="text-sm text-gray-600 mb-4 space-y-1">
                            <li>• Universal Testing Machine</li>
                            <li>• Impact Tester</li>
                            <li>• Abrasion Tester</li>
                            <li>• Hardness Tester</li>
                        </ul>
                        <a href="#mechanical-details" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Learn More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Climatic & Environmental Chambers -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gradient-to-br from-green-100 to-green-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="thermometer-snowflake" class="h-20 w-20 text-green-500 group-hover:scale-110 transition-transform"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-3">Climatic & Environmental Chambers</h3>
                        <p class="text-gray-600 mb-4">Precision environmental simulation chambers for temperature, humidity, and climatic testing across extreme conditions.</p>
                        <ul class="text-sm text-gray-600 mb-4 space-y-1">
                            <li>• Temperature Chamber</li>
                            <li>• Humidity Chamber</li>
                            <li>• Thermal Shock Chamber</li>
                            <li>• Salt Spray Chamber</li>
                        </ul>
                        <a href="#climatic-details" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Learn More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Optical & Chemical Tests -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gradient-to-br from-purple-100 to-purple-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="eye" class="h-20 w-20 text-purple-500 group-hover:scale-110 transition-transform"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-3">Optical & Chemical Tests</h3>
                        <p class="text-gray-600 mb-4">Advanced optical measurement systems and chemical analysis equipment for material characterization.</p>
                        <ul class="text-sm text-gray-600 mb-4 space-y-1">
                            <li>• Spectrophotometer</li>
                            <li>• Colorimeter</li>
                            <li>• Refractometer</li>
                            <li>• Chemical Analyzer</li>
                        </ul>
                        <a href="#optical-details" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Learn More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Electrical Tests -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gradient-to-br from-yellow-100 to-yellow-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="zap" class="h-20 w-20 text-yellow-500 group-hover:scale-110 transition-transform"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-3">Electrical Tests</h3>
                        <p class="text-gray-600 mb-4">Comprehensive electrical testing equipment for conductivity, insulation, and electrical safety compliance.</p>
                        <ul class="text-sm text-gray-600 mb-4 space-y-1">
                            <li>• Insulation Tester</li>
                            <li>• Dielectric Strength Tester</li>
                            <li>• Resistance Meter</li>
                            <li>• Electrical Safety Analyzer</li>
                        </ul>
                        <a href="#electrical-details" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Learn More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Sample Preparation -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 overflow-hidden group">
                    <div class="h-48 bg-gradient-to-br from-indigo-100 to-indigo-200 relative overflow-hidden flex items-center justify-center">
                        <i data-lucide="layers" class="h-20 w-20 text-indigo-500 group-hover:scale-110 transition-transform"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-900 mb-3">Sample Preparation</h3>
                        <p class="text-gray-600 mb-4">Precision equipment for sample preparation, cutting, polishing, and conditioning for accurate testing results.</p>
                        <ul class="text-sm text-gray-600 mb-4 space-y-1">
                            <li>• Sample Cutter</li>
                            <li>• Grinding Machine</li>
                            <li>• Polishing Equipment</li>
                            <li>• Conditioning Chamber</li>
                        </ul>
                        <a href="#sample-details" class="text-blue-600 font-semibold hover:text-blue-800 inline-flex items-center">
                            Learn More <i data-lucide="arrow-right" class="h-4 w-4 ml-1"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Why Choose Our Products?</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i data-lucide="shield-check" class="h-8 w-8 text-blue-600"></i>
                    </div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Standard Compliance</h4>
                    <p class="text-gray-600">All products meet international testing standards (ASTM, ISO, IEC, etc.)</p>
                </div>
                <div class="text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i data-lucide="settings" class="h-8 w-8 text-blue-600"></i>
                    </div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Precision Engineering</h4>
                    <p class="text-gray-600">Built with high-precision components for accurate and reliable results</p>
                </div>
                <div class="text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i data-lucide="headphones" class="h-8 w-8 text-blue-600"></i>
                    </div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Expert Support</h4>
                    <p class="text-gray-600">Comprehensive technical support and training for all our products</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-gray-300 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div class="col-span-1 md:col-span-2">
                    <div class="flex items-center gap-2 mb-4">
                        <i data-lucide="cpu" class="h-6 w-6 text-blue-500"></i>
                        <span class="font-bold text-lg text-white">SRS MECHATRONICS</span>
                    </div>
                    <p class="text-sm text-gray-400 max-w-sm mb-4">
                        Trusted name in quality test instruments. We manufacture standard-compliant test equipment with excellent reliability and performance globally.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="linkedin" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="twitter" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="mail" class="h-5 w-5"></i></a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-white font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/" class="hover:text-blue-400 transition-colors">Home</a></li>
                        <li><a href="/about" class="hover:text-blue-400 transition-colors">About Us</a></li>
                        <li><a href="/products" class="hover:text-blue-400 transition-colors">Products</a></li>
                        <li><a href="/services" class="hover:text-blue-400 transition-colors">Services</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold mb-4">Contact Info</h4>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <i data-lucide="map-pin" class="h-4 w-4 mr-2 mt-0.5 text-blue-500 flex-shrink-0"></i>
                            <span>Delhi, India</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="phone" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>+91 XXXXX XXXXX</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="mail" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>info@srsmechatronics.com</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 text-center text-sm text-gray-500">
                <p>&copy; 2026 SRS Mechatronics Instrumentations. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleDropdown() {
            const dropdown = document.getElementById('products-dropdown');
            const isVisible = dropdown.classList.contains('opacity-100');
            
            if (isVisible) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            } else {
                dropdown.classList.remove('opacity-0', 'invisible');
                dropdown.classList.add('opacity-100', 'visible');
            }
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const dropdown = document.getElementById('products-dropdown');
            const button = event.target.closest('button');
            
            if (!button || !button.onclick || button.onclick.toString().indexOf('toggleDropdown') === -1) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            }
        });

        lucide.createIcons();
    </script>
</body>
</html>
"""

SERVICES_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services - SRS MECHATRONICS INSTRUMENTATIONS</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .hero-pattern {
            background-color: #0f172a;
            background-image: radial-gradient(#1e293b 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .fade-in { animation: fadeIn 1.5s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

    <!-- Navigation Bar -->
    <nav class="bg-white shadow-md fixed w-full z-50 top-0">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex items-center gap-2">
                        <i data-lucide="cpu" class="h-8 w-8 text-blue-700"></i>
                        <span class="font-bold text-xl tracking-tight text-blue-900 leading-tight">
                            SRS MECHATRONICS<br><span class="text-sm font-medium text-gray-500">INSTRUMENTATIONS</span>
                        </span>
                    </div>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Home</a>
                    <a href="/about" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">About Us</a>
                    <div class="relative">
                        <button class="text-gray-700 hover:text-blue-700 font-medium transition-colors flex items-center gap-1" onclick="toggleDropdown()">
                            Products <i data-lucide="chevron-down" class="h-4 w-4"></i>
                        </button>
                        <div id="products-dropdown" class="absolute top-full left-0 mt-2 w-64 bg-white rounded-md shadow-lg border border-gray-200 opacity-0 invisible transform translate-y-2 transition-all duration-200 z-50">
                            <div class="py-2">
                                <a href="/products#chemical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flask-conical" class="h-4 w-4 inline mr-2"></i>Chemical Tests
                                </a>
                                <a href="/products#electrical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="zap" class="h-4 w-4 inline mr-2"></i>Electrical Tests
                                </a>
                                <a href="/products#environmental" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="thermometer" class="h-4 w-4 inline mr-2"></i>Environmental Tests
                                </a>
                                <a href="/products#fire-smoke" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flame" class="h-4 w-4 inline mr-2"></i>Fire and Smoke Tests
                                </a>
                                <a href="/products#optical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="eye" class="h-4 w-4 inline mr-2"></i>Optical Tests
                                </a>
                                <a href="/products#sample-prep" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="test-tube" class="h-4 w-4 inline mr-2"></i>Sample Preparation
                                </a>
                            </div>
                        </div>
                    </div>
                    <a href="/services" class="text-blue-700 font-medium transition-colors">Services</a>
                    <a href="/contact" class="bg-blue-700 text-white px-5 py-2 rounded-md hover:bg-blue-800 transition-colors font-medium">Contact Us</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-pattern pt-32 pb-20 text-white min-h-[50vh] flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 fade-in">
            <div class="max-w-4xl">
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight">
                    Our Services
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 leading-relaxed">
                    Comprehensive support services to ensure optimal performance of your testing equipment throughout its lifecycle.
                </p>
            </div>
        </div>
    </section>

    <!-- Services Grid -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Complete Testing Solutions</h2>
                <div class="h-1 w-20 bg-blue-600 mx-auto mb-6"></div>
                <p class="text-gray-600 max-w-2xl mx-auto">From consultation to maintenance, we provide end-to-end services to support your testing requirements.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Consulting & Engineering -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 p-6">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="brain" class="h-8 w-8 text-blue-600"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Consulting & Engineering</h3>
                    <p class="text-gray-600 mb-4">Expert guidance on test method selection, equipment specification, and testing protocol development for your specific applications.</p>
                    <ul class="text-sm text-gray-600 space-y-1 mb-4">
                        <li>• Test Method Optimization</li>
                        <li>• Equipment Selection</li>
                        <li>• Protocol Development</li>
                        <li>• Compliance Consulting</li>
                    </ul>
                </div>

                <!-- Installation & Commissioning -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 p-6">
                    <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="wrench" class="h-8 w-8 text-green-600"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Installation & Commissioning</h3>
                    <p class="text-gray-600 mb-4">Professional installation services with comprehensive commissioning to ensure your equipment operates at peak performance.</p>
                    <ul class="text-sm text-gray-600 space-y-1 mb-4">
                        <li>• Site Preparation</li>
                        <li>• Equipment Installation</li>
                        <li>• Calibration & Testing</li>
                        <li>• Performance Verification</li>
                    </ul>
                </div>

                <!-- Training & Education -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 p-6">
                    <div class="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="graduation-cap" class="h-8 w-8 text-purple-600"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Training & Education</h3>
                    <p class="text-gray-600 mb-4">Comprehensive training programs for operators, technicians, and quality managers to maximize equipment utilization.</p>
                    <ul class="text-sm text-gray-600 space-y-1 mb-4">
                        <li>• Operator Training</li>
                        <li>• Maintenance Training</li>
                        <li>• Advanced Applications</li>
                        <li>• Certification Programs</li>
                    </ul>
                </div>

                <!-- Maintenance & Support -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 p-6">
                    <div class="bg-orange-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="shield" class="h-8 w-8 text-orange-600"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Maintenance & Support</h3>
                    <p class="text-gray-600 mb-4">Preventive maintenance programs and 24/7 technical support to minimize downtime and ensure continuous operation.</p>
                    <ul class="text-sm text-gray-600 space-y-1 mb-4">
                        <li>• Preventive Maintenance</li>
                        <li>• Emergency Repairs</li>
                        <li>• Spare Parts Supply</li>
                        <li>• Remote Diagnostics</li>
                    </ul>
                </div>

                <!-- Calibration Services -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 p-6">
                    <div class="bg-red-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="target" class="h-8 w-8 text-red-600"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Calibration Services</h3>
                    <p class="text-gray-600 mb-4">Traceable calibration services with accredited laboratories to maintain measurement accuracy and compliance.</p>
                    <ul class="text-sm text-gray-600 space-y-1 mb-4">
                        <li>• ISO/IEC 17025 Accredited</li>
                        <li>• Traceable Standards</li>
                        <li>• Calibration Certificates</li>
                        <li>• Regular Recalibration</li>
                    </ul>
                </div>

                <!-- Custom Solutions -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100 p-6">
                    <div class="bg-indigo-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-lucide="lightbulb" class="h-8 w-8 text-indigo-600"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Custom Solutions</h3>
                    <p class="text-gray-600 mb-4">Tailored testing solutions and modifications to meet unique application requirements and industry-specific needs.</p>
                    <ul class="text-sm text-gray-600 space-y-1 mb-4">
                        <li>• Custom Test Fixtures</li>
                        <li>• Software Integration</li>
                        <li>• Automation Solutions</li>
                        <li>• Special Applications</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-gray-300 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div class="col-span-1 md:col-span-2">
                    <div class="flex items-center gap-2 mb-4">
                        <i data-lucide="cpu" class="h-6 w-6 text-blue-500"></i>
                        <span class="font-bold text-lg text-white">SRS MECHATRONICS</span>
                    </div>
                    <p class="text-sm text-gray-400 max-w-sm mb-4">
                        Trusted name in quality test instruments. We manufacture standard-compliant test equipment with excellent reliability and performance globally.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="linkedin" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="twitter" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="mail" class="h-5 w-5"></i></a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-white font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/" class="hover:text-blue-400 transition-colors">Home</a></li>
                        <li><a href="/about" class="hover:text-blue-400 transition-colors">About Us</a></li>
                        <li><a href="/products" class="hover:text-blue-400 transition-colors">Products</a></li>
                        <li><a href="/services" class="hover:text-blue-400 transition-colors">Services</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold mb-4">Contact Info</h4>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <i data-lucide="map-pin" class="h-4 w-4 mr-2 mt-0.5 text-blue-500 flex-shrink-0"></i>
                            <span>Delhi, India</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="phone" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>+91 XXXXX XXXXX</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="mail" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>info@srsmechatronics.com</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 text-center text-sm text-gray-500">
                <p>&copy; 2026 SRS Mechatronics Instrumentations. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleDropdown() {
            const dropdown = document.getElementById('products-dropdown');
            const isVisible = dropdown.classList.contains('opacity-100');
            
            if (isVisible) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            } else {
                dropdown.classList.remove('opacity-0', 'invisible');
                dropdown.classList.add('opacity-100', 'visible');
            }
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const dropdown = document.getElementById('products-dropdown');
            const button = event.target.closest('button');
            
            if (!button || !button.onclick || button.onclick.toString().indexOf('toggleDropdown') === -1) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            }
        });

        lucide.createIcons();
    </script>
</body>
</html>
"""

CONTACT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - SRS MECHATRONICS INSTRUMENTATIONS</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .hero-pattern {
            background-color: #0f172a;
            background-image: radial-gradient(#1e293b 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .fade-in { animation: fadeIn 1.5s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">

    <!-- Navigation Bar -->
    <nav class="bg-white shadow-md fixed w-full z-50 top-0">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex items-center gap-2">
                        <i data-lucide="cpu" class="h-8 w-8 text-blue-700"></i>
                        <span class="font-bold text-xl tracking-tight text-blue-900 leading-tight">
                            SRS MECHATRONICS<br><span class="text-sm font-medium text-gray-500">INSTRUMENTATIONS</span>
                        </span>
                    </div>
                </div>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Home</a>
                    <a href="/about" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">About Us</a>
                    <div class="relative">
                        <button class="text-gray-700 hover:text-blue-700 font-medium transition-colors flex items-center gap-1" onclick="toggleDropdown()">
                            Products <i data-lucide="chevron-down" class="h-4 w-4"></i>
                        </button>
                        <div id="products-dropdown" class="absolute top-full left-0 mt-2 w-64 bg-white rounded-md shadow-lg border border-gray-200 opacity-0 invisible transform translate-y-2 transition-all duration-200 z-50">
                            <div class="py-2">
                                <a href="/products#chemical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flask-conical" class="h-4 w-4 inline mr-2"></i>Chemical Tests
                                </a>
                                <a href="/products#electrical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="zap" class="h-4 w-4 inline mr-2"></i>Electrical Tests
                                </a>
                                <a href="/products#environmental" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="thermometer" class="h-4 w-4 inline mr-2"></i>Environmental Tests
                                </a>
                                <a href="/products#fire-smoke" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="flame" class="h-4 w-4 inline mr-2"></i>Fire and Smoke Tests
                                </a>
                                <a href="/products#optical" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="eye" class="h-4 w-4 inline mr-2"></i>Optical Tests
                                </a>
                                <a href="/products#sample-prep" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors">
                                    <i data-lucide="test-tube" class="h-4 w-4 inline mr-2"></i>Sample Preparation
                                </a>
                            </div>
                        </div>
                    </div>
                    <a href="/services" class="text-gray-700 hover:text-blue-700 font-medium transition-colors">Services</a>
                    <a href="/contact" class="text-blue-700 font-medium transition-colors">Contact Us</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-pattern pt-32 pb-20 text-white min-h-[50vh] flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 fade-in">
            <div class="max-w-4xl">
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight">
                    Contact Us
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-10 leading-relaxed">
                    Ready to elevate your testing capabilities? Get in touch with our experts for personalized solutions and support.
                </p>
            </div>
        </div>
    </section>

    <!-- Contact Form and Info -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <!-- Contact Form -->
                <div>
                    <h2 class="text-3xl font-bold text-gray-900 mb-6">Send us a Message</h2>
                    <div class="h-1 w-20 bg-blue-600 mb-8"></div>
                    <form class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Name *</label>
                                <input type="text" class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" required>
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
                                <input type="email" class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" required>
                            </div>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
                                <input type="tel" class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Company</label>
                                <input type="text" class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500">
                            </div>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Subject *</label>
                            <select class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" required>
                                <option value="">Select a subject</option>
                                <option value="product-inquiry">Product Inquiry</option>
                                <option value="service-request">Service Request</option>
                                <option value="technical-support">Technical Support</option>
                                <option value="quote-request">Quote Request</option>
                                <option value="partnership">Partnership Opportunity</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Message *</label>
                            <textarea rows="6" class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" placeholder="Tell us about your requirements..." required></textarea>
                        </div>
                        <button type="button" onclick="alert('Thank you for your message! We will get back to you within 24 hours.')" class="w-full bg-blue-700 text-white font-bold py-4 px-6 rounded-md hover:bg-blue-800 transition-colors text-lg">
                            Send Message
                        </button>
                    </form>
                </div>

                <!-- Contact Information -->
                <div>
                    <h2 class="text-3xl font-bold text-gray-900 mb-6">Get in Touch</h2>
                    <div class="h-1 w-20 bg-blue-600 mb-8"></div>
                    
                    <div class="space-y-8">
                        <div class="flex items-start">
                            <div class="bg-blue-100 p-3 rounded-full mr-4">
                                <i data-lucide="map-pin" class="h-6 w-6 text-blue-600"></i>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-gray-900 mb-1">Head Office</h4>
                                <p class="text-gray-600">SRS Mechatronics Instrumentations Pvt. Ltd.<br>
                                123 Industrial Area, Phase-II<br>
                                Delhi - 110020, India</p>
                            </div>
                        </div>

                        <div class="flex items-start">
                            <div class="bg-blue-100 p-3 rounded-full mr-4">
                                <i data-lucide="phone" class="h-6 w-6 text-blue-600"></i>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-gray-900 mb-1">Phone</h4>
                                <p class="text-gray-600">+91 11 1234 5678<br>
                                +91 98765 43210 (Mobile)</p>
                            </div>
                        </div>

                        <div class="flex items-start">
                            <div class="bg-blue-100 p-3 rounded-full mr-4">
                                <i data-lucide="mail" class="h-6 w-6 text-blue-600"></i>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-gray-900 mb-1">Email</h4>
                                <p class="text-gray-600">info@srsmechatronics.com<br>
                                sales@srsmechatronics.com<br>
                                support@srsmechatronics.com</p>
                            </div>
                        </div>

                        <div class="flex items-start">
                            <div class="bg-blue-100 p-3 rounded-full mr-4">
                                <i data-lucide="clock" class="h-6 w-6 text-blue-600"></i>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-gray-900 mb-1">Business Hours</h4>
                                <p class="text-gray-600">Monday - Friday: 9:00 AM - 6:00 PM<br>
                                Saturday: 9:00 AM - 2:00 PM<br>
                                Sunday: Closed</p>
                            </div>
                        </div>
                    </div>

                    <!-- Map Placeholder -->
                    <div class="mt-8 bg-gray-200 rounded-lg h-64 flex items-center justify-center">
                        <div class="text-center">
                            <i data-lucide="map" class="h-12 w-12 text-gray-400 mx-auto mb-2"></i>
                            <p class="text-gray-500">Interactive Map</p>
                            <p class="text-sm text-gray-400">Delhi, India</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-gray-300 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
                <div class="col-span-1 md:col-span-2">
                    <div class="flex items-center gap-2 mb-4">
                        <i data-lucide="cpu" class="h-6 w-6 text-blue-500"></i>
                        <span class="font-bold text-lg text-white">SRS MECHATRONICS</span>
                    </div>
                    <p class="text-sm text-gray-400 max-w-sm mb-4">
                        Trusted name in quality test instruments. We manufacture standard-compliant test equipment with excellent reliability and performance globally.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="linkedin" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="twitter" class="h-5 w-5"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i data-lucide="mail" class="h-5 w-5"></i></a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-white font-bold mb-4">Quick Links</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/" class="hover:text-blue-400 transition-colors">Home</a></li>
                        <li><a href="/about" class="hover:text-blue-400 transition-colors">About Us</a></li>
                        <li><a href="/products" class="hover:text-blue-400 transition-colors">Products</a></li>
                        <li><a href="/services" class="hover:text-blue-400 transition-colors">Services</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-bold mb-4">Contact Info</h4>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start">
                            <i data-lucide="map-pin" class="h-4 w-4 mr-2 mt-0.5 text-blue-500 flex-shrink-0"></i>
                            <span>Delhi, India</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="phone" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>+91 XXXXX XXXXX</span>
                        </li>
                        <li class="flex items-center">
                            <i data-lucide="mail" class="h-4 w-4 mr-2 text-blue-500"></i>
                            <span>info@srsmechatronics.com</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-slate-800 pt-8 text-center text-sm text-gray-500">
                <p>&copy; 2026 SRS Mechatronics Instrumentations. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleDropdown() {
            const dropdown = document.getElementById('products-dropdown');
            const isVisible = dropdown.classList.contains('opacity-100');
            
            if (isVisible) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            } else {
                dropdown.classList.remove('opacity-0', 'invisible');
                dropdown.classList.add('opacity-100', 'visible');
            }
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            const dropdown = document.getElementById('products-dropdown');
            const button = event.target.closest('button');
            
            if (!button || !button.onclick || button.onclick.toString().indexOf('toggleDropdown') === -1) {
                dropdown.classList.remove('opacity-100', 'visible');
                dropdown.classList.add('opacity-0', 'invisible');
            }
        });

        lucide.createIcons();
    </script>
</body>
</html>
"""

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the generated HTML strings based on the path
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HOME_HTML.encode("utf8"))
        elif self.path == '/about':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(ABOUT_HTML.encode("utf8"))
        elif self.path == '/products':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(PRODUCTS_HTML.encode("utf8"))
        elif self.path == '/services':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(SERVICES_HTML.encode("utf8"))
        elif self.path == '/contact':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(CONTACT_HTML.encode("utf8"))
        else:
            # Fallback to standard behavior if looking for specific local files (like favicons)
            super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    handler_object = MyHttpRequestHandler
    my_server = socketserver.TCPServer(("", PORT), handler_object)
    
    print(f"\\n===============================================")
    print(f"Server successfully started!")
    print(f"Please open your browser to: http://localhost:{PORT}")
    print(f"Press Ctrl+C to stop the server.")
    print(f"===============================================\\n")
    
    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        print("\\nShutting down server...")
        my_server.server_close()
        print("Server successfully stopped.")

