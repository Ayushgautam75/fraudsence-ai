#!/usr/bin/env python
"""
Quick UI Preview & Verification Script
"""
import sys
from pathlib import Path

def verify_ui_files():
    """Verify all UI files exist"""
    print("\n" + "="*60)
    print("🎨 MODERN UI VERIFICATION")
    print("="*60 + "\n")
    
    base_dir = Path(__file__).parent
    ui_files = {
        "Templates": [
            "templates/dashboard_modern.html",
            "templates/login_modern.html",
        ],
        "Styles": [
            "static/css/dashboard_modern.css",
        ],
        "Documentation": [
            "UI_MODERNIZATION_GUIDE.md",
            "UI_COMPLETE_SUMMARY.md",
        ]
    }
    
    all_ok = True
    
    for category, files in ui_files.items():
        print(f"\n📁 {category}:")
        for file in files:
            path = base_dir / file
            if path.exists():
                size = path.stat().st_size
                size_kb = size / 1024
                print(f"  ✅ {file} ({size_kb:.1f} KB)")
            else:
                print(f"  ❌ {file}")
                all_ok = False
    
    return all_ok

def check_app_config():
    """Check app.py uses modern templates"""
    print("\n📋 App Configuration Check:")
    
    app_file = Path(__file__).parent / "app.py"
    content = app_file.read_text(encoding='utf-8', errors='ignore')
    
    checks = {
        "Using modern dashboard": "dashboard_modern.html" in content,
        "Using modern login": "login_modern.html" in content,
    }
    
    all_ok = True
    for check, result in checks.items():
        status = "✅" if result else "❌"
        print(f"  {status} {check}")
        all_ok = all_ok and result
    
    return all_ok

def display_ui_features():
    """Display UI features"""
    print("\n✨ Modern UI Features:")
    
    features = [
        "Professional gradient sidebar",
        "Responsive dashboard layout",
        "Beautiful KPI cards",
        "Interactive charts (5 types)",
        "Organized prediction forms",
        "Alert center",
        "Transaction table",
        "Modern login page",
        "Smooth animations",
        "Professional color scheme",
    ]
    
    for feature in features:
        print(f"  ✅ {feature}")

def display_usage():
    """Display how to use"""
    print("\n" + "="*60)
    print("🚀 HOW TO USE THE NEW UI")
    print("="*60)
    
    instructions = """
1. START THE APPLICATION
   Command: python app.py
   
2. OPEN IN BROWSER
   URL: http://127.0.0.1:5000/
   
3. LOGIN
   Username: admin
   Password: demo123
   
   (Also try: analyst / demo123 or reviewer / demo123)
   
4. EXPLORE THE DASHBOARD
   - View KPI metrics
   - Check fraud trends
   - See recent transactions
   - Make predictions
   - Analyze patterns
   
5. USE PREDICTION FORMS
   - Fraud Detection
   - Loan Default
   - Risk Score
   - Anomaly Detection
   - Spending Pattern
    """
    
    print(instructions)

def display_features():
    """Display feature breakdown"""
    print("\n" + "="*60)
    print("📊 DASHBOARD FEATURES")
    print("="*60 + "\n")
    
    features = {
        "Navigation": ["Sidebar menu", "Quick links", "User profile"],
        "Metrics": ["Total transactions", "Fraud alerts", "Safe transactions", "Model accuracy"],
        "Visualizations": [
            "Fraud trend (line chart)",
            "Fraud over time (bar chart)",
            "Location-based fraud (bar chart)",
            "Risk distribution (doughnut)",
            "Transaction patterns (radar)"
        ],
        "Tables": ["Recent transactions", "Status indicators", "Confidence scores"],
        "Forms": [
            "Fraud Detection",
            "Loan Prediction",
            "Risk Score",
            "Anomaly Detection",
            "Spending Pattern"
        ]
    }
    
    for category, items in features.items():
        print(f"{category}:")
        for item in items:
            print(f"  • {item}")
        print()

def main():
    """Main verification"""
    print("\n" + "="*70)
    print("             🛡️ FRAUDSENSE AI - MODERN UI READY              ")
    print("="*70)
    
    # Check files
    files_ok = verify_ui_files()
    
    # Check app config
    config_ok = check_app_config()
    
    # Display features
    display_ui_features()
    
    # Display feature breakdown
    display_features()
    
    # Display usage
    display_usage()
    
    # Summary
    print("\n" + "="*60)
    print("✅ VERIFICATION SUMMARY")
    print("="*60)
    print(f"Files OK:      {'✅ YES' if files_ok else '❌ NO'}")
    print(f"Config OK:     {'✅ YES' if config_ok else '❌ NO'}")
    print("\n" + "="*60)
    
    if files_ok and config_ok:
        print("🎉 MODERN UI IS READY TO USE!")
        print("\nStart with: python app.py")
        print("Then open: http://127.0.0.1:5000/")
        print("="*60 + "\n")
        return 0
    else:
        print("⚠️  SOME CHECKS FAILED")
        print("="*60 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
