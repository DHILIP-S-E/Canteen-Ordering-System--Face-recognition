import streamlit as st
import pandas as pd
from datetime import datetime

def set_custom_theme():
    """Apply custom theme and styling to the entire application"""
    st.markdown("""
        <style>
        /* Main theme colors */
        :root {
            --primary-color: #2ecc71;
            --secondary-color: #3498db;
            --background-color: #f8f9fa;
            --text-color: #2c3e50;
        }

        /* Global styles */
        .stApp {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }

        /* Enhanced Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%) !important;
            padding: 2rem 1rem;
            border-right: 2px solid #2ecc71;
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
            color: #ffffff !important;
        }

        /* Make sidebar text and elements more visible */
        [data-testid="stSidebar"] .stSelectbox label,
        [data-testid="stSidebar"] .stTextInput label {
            color: #ffffff !important;
            font-weight: 500;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }

        [data-testid="stSidebar"] .stButton > button {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-weight: 500;
            width: 100%;
            margin: 0.5rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            background: linear-gradient(135deg, #27ae60 0%, #219a52 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }

        /* Sidebar navigation links */
        [data-testid="stSidebar"] a {
            color: #ffffff !important;
            text-decoration: none;
            padding: 0.5rem;
            display: block;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        [data-testid="stSidebar"] a:hover {
            background: rgba(46, 204, 113, 0.2);
            padding-left: 1rem;
        }

        /* Sidebar section headers */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #2ecc71 !important;
            margin-top: 1.5rem;
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }

        /* Sidebar input fields */
        [data-testid="stSidebar"] input[type="text"],
        [data-testid="stSidebar"] select {
            background: rgba(255, 255, 255, 0.1) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: white !important;
            border-radius: 5px;
        }

        [data-testid="stSidebar"] input[type="text"]:focus,
        [data-testid="stSidebar"] select:focus {
            border-color: #2ecc71 !important;
            box-shadow: 0 0 0 2px rgba(46, 204, 113, 0.3) !important;
        }

        /* Sidebar separators */
        [data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.1);
            margin: 1.5rem 0;
        }

        /* Card styling with gradient */
        .custom-card, .cart-item, .order-status, .history-card, .notification-card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid rgba(0,0,0,0.1);
            margin: 1rem 0;
            padding: 1.2rem;
        }
        
        .custom-card:hover, .cart-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        /* Button Styling with gradient */
        .stButton > button {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            color: white;
            border-radius: 25px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(46,204,113,0.4);
            background: linear-gradient(135deg, #27ae60 0%, #219a52 100%);
        }

        /* Status badges with gradients */
        .status-placed {
            background: linear-gradient(135deg, #f1c40f 0%, #f39c12 100%);
        }
        
        .status-preparing {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
        }
        
        .status-prepared {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        }

        /* Cart styling */
        .cart-total {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            color: white;
            padding: 1rem;
            border-radius: 15px;
            margin-top: 1rem;
            font-size: 1.2rem;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 15px rgba(46,204,113,0.3);
        }

        /* Input Styling */
        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #e9ecef;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }

        .stTextInput > div > div > input:focus {
            border-color: #2ecc71;
            box-shadow: 0 0 0 2px rgba(46,204,113,0.2);
        }

        /* Notification styling */
        .notification-card {
            border-left: 4px solid #3498db;
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        }

        .notification-card.unread {
            border-left: 4px solid #2ecc71;
            background: linear-gradient(145deg, #e3f2fd 0%, #bbdefb 100%);
        }

        /* Menu item cards */
        .menu-item {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            transition: all 0.3s ease;
        }

        .menu-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: linear-gradient(90deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 0.5rem;
            border-radius: 15px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 10px;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(46,204,113,0.1);
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%) !important;
            color: white !important;
        }

        /* Metric styling */
        [data-testid="stMetricValue"] {
            background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }

        </style>
    """, unsafe_allow_html=True)

def display_menu(menu_items, add_to_cart_callback):
    """Display menu items with enhanced card design and visual appeal"""
    # Custom CSS for menu items
    st.markdown("""
        <style>
        .menu-card {
            background: white;
            border-radius: 12px;
            padding: 1.2rem;
            margin: 0.8rem 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border: 1px solid #eee;
            height: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .menu-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.15);
        }
        
        .menu-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 0.8rem;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
        }
        
        .menu-price {
            font-size: 1.2rem;
            font-weight: 700;
            color: #2ecc71;
            margin: 0.5rem 0;
        }
        
        .menu-category {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            background: #f8f9fa;
            border-radius: 15px;
            font-size: 0.85rem;
            color: #7f8c8d;
            margin-bottom: 0.8rem;
        }
        
        .menu-stock {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.85rem;
            margin-left: 0.5rem;
        }
        
        .in-stock {
            background: #e8f5e9;
            color: #2e7d32;
        }
        
        .low-stock {
            background: #fff8e1;
            color: #f57f17;
        }
        
        .out-stock {
            background: #ffebee;
            color: #c62828;
        }
        
        .menu-image-container {
            height: 180px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border-radius: 8px;
            margin-bottom: 1rem;
            background: #f8f9fa;
        }
        
        .menu-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        
        .menu-image:hover {
            transform: scale(1.05);
        }
        
        .menu-details {
            margin: 1rem 0;
        }
        
        .menu-actions {
            margin-top: 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .quantity-selector {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .add-btn {
            background: #3498db;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-weight: 500;
        }
        
        .add-btn:hover {
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .out-of-stock-badge {
            position: absolute;
            top: 10px;
            right: 10px;
            background: #e74c3c;
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-weight: 500;
            transform: rotate(5deg);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Create a grid layout for menu items
    cols = st.columns(3)
    
    for idx, item in menu_items.iterrows():
        with cols[idx % 3]:
            # Determine stock status for styling
            if item['stock'] <= 0:
                stock_class = "out-stock"
                stock_text = "Out of Stock"
            elif item['stock'] < 5:
                stock_class = "low-stock"
                stock_text = f"Low Stock: {item['stock']}"
            else:
                stock_class = "in-stock"
                stock_text = f"In Stock: {item['stock']}"
            
            # Start custom HTML for menu card
            st.markdown(f"""
                <div class="menu-card fade-in">
                    <div class="menu-title">{item['name']}</div>
            """, unsafe_allow_html=True)
            
            # Display image if available
            image_url = item.get('image_url', '')
            if image_url:
                try:
                    st.markdown(f"""
                        <div class="menu-image-container">
                            <img src="{image_url}" class="menu-image" alt="{item['name']}">
                        </div>
                    """, unsafe_allow_html=True)
                except Exception:
                    st.markdown("""
                        <div class="menu-image-container">
                            <div style="text-align: center; padding: 2rem;">
                                <span style="font-size: 2rem;">🍽️</span><br>
                                <span style="color: #7f8c8d;">Image not available</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                # Display a placeholder if no image
                st.markdown(f"""
                    <div class="menu-image-container">
                        <div style="text-align: center; padding: 2rem;">
                            <span style="font-size: 2rem;">🍽️</span><br>
                            <span style="color: #7f8c8d;">No image available</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Display price with emphasis
            st.markdown(f"""
                <div class="menu-price">₹{item['price']:.2f}</div>
                <div>
                    <span class="menu-category">{item['category']}</span>
                    <span class="menu-stock {stock_class}">{stock_text}</span>
                </div>
            """, unsafe_allow_html=True)
            
            # Add to cart section
            if item['stock'] > 0:
                # Use Streamlit components for interactive elements
                with st.container():
                    st.markdown('<div class="menu-actions">', unsafe_allow_html=True)
                    quantity = st.number_input(
                        "Quantity",
                        min_value=1,
                        max_value=item['stock'],
                        value=1,
                        key=f"qty_{item['id']}"
                    )
                    if st.button("🛒 Add to Cart", key=f"add_{item['id']}"):
                        add_to_cart_callback(item, quantity)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="out-of-stock-badge">Out of Stock</div>
                """, unsafe_allow_html=True)
            
            # Close the card div
            st.markdown("</div>", unsafe_allow_html=True)

def display_cart(cart_items, on_remove):
    """Display shopping cart with enhanced styling and animations"""
    st.markdown("""
        <style>
        .cart-container {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin: 1.5rem 0;
            border: 1px solid #eee;
        }
        
        .cart-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 0.8rem;
            border-bottom: 2px solid #3498db;
        }
        
        .cart-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2c3e50;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .cart-item {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            margin: 0.8rem 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            border-left: 4px solid #3498db;
            animation: slideIn 0.5s ease-out;
        }
        
        .cart-item:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
        
        .cart-item-details {
            flex: 1;
        }
        
        .cart-item-name {
            font-weight: 600;
            color: #2c3e50;
            font-size: 1.1rem;
            margin-bottom: 0.3rem;
        }
        
        .cart-item-meta {
            color: #7f8c8d;
            font-size: 0.9rem;
        }
        
        .cart-item-price {
            font-weight: 700;
            color: #2ecc71;
            font-size: 1.1rem;
            text-align: right;
            min-width: 80px;
        }
        
        .cart-total {
            background: linear-gradient(135deg, #2ecc71, #27ae60);
            color: white;
            padding: 1.2rem;
            border-radius: 10px;
            margin-top: 1.5rem;
            font-size: 1.3rem;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2); }
            50% { box-shadow: 0 4px 20px rgba(46, 204, 113, 0.4); }
            100% { box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2); }
        }
        
        .cart-empty {
            text-align: center;
            padding: 3rem 2rem;
            background: #f8f9fa;
            border-radius: 12px;
            margin: 2rem 0;
            color: #7f8c8d;
            border: 2px dashed #bdc3c7;
        }
        
        .cart-empty-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            color: #bdc3c7;
        }
        
        .cart-empty-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #34495e;
        }
        
        .cart-empty-text {
            font-size: 1rem;
            max-width: 80%;
            margin: 0 auto;
        }
        
        .cart-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 0.5rem;
        }
        
        .remove-btn {
            background: none;
            border: none;
            color: #e74c3c;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.3rem;
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }
        
        .remove-btn:hover {
            background: #ffebee;
            transform: translateY(-2px);
        }
        
        .cart-badge {
            background: #3498db;
            color: white;
            border-radius: 50%;
            width: 25px;
            height: 25px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
            margin-left: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Start cart container
    st.markdown("""
        <div class="cart-container fade-in">
            <div class="cart-header">
                <div class="cart-title">
                    🛒 Your Cart
                    <span class="cart-badge">{}</span>
                </div>
            </div>
    """.format(len(cart_items)), unsafe_allow_html=True)
    
    if not cart_items:
        st.markdown("""
            <div class="cart-empty slide-in">
                <div class="cart-empty-icon">🛒</div>
                <div class="cart-empty-title">Your cart is empty</div>
                <div class="cart-empty-text">
                    Browse our delicious menu and add some items to get started!
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)  # Close cart container
        return 0
    
    total = 0
    
    for item in cart_items:
        item_total = item['price'] * item['quantity']
        total += item_total
        
        st.markdown(f"""
            <div class="cart-item">
                <div class="cart-item-details">
                    <div class="cart-item-name">{item['name']}</div>
                    <div class="cart-item-meta">
                        Quantity: {item['quantity']} × ₹{item['price']:.2f}
                    </div>
                </div>
                <div class="cart-item-price">
                    ₹{item_total:.2f}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Remove button using Streamlit component for interactivity
        col1, col2, col3 = st.columns([6, 2, 2])
        with col3:
            if st.button("🗑️ Remove", key=f"remove_{item['id']}"):
                on_remove(item)
    
    # Display total with animation
    st.markdown(f"""
        <div class="cart-total">
            Total Amount: ₹{total:.2f}
        </div>
    """, unsafe_allow_html=True)
    
    # Close cart container
    st.markdown("</div>", unsafe_allow_html=True)
    
    return total

def display_order_status(order_id, status):
    """Display order status with enhanced visual design and timeline"""
    st.markdown("""
        <style>
        .order-status-container {
            background: white;
            border-radius: 12px;
            padding: 1.8rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 1.5rem 0;
            position: relative;
            overflow: hidden;
            border: 1px solid #eee;
        }
        
        .order-status-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(to right, #3498db, #2ecc71);
        }
        
        .order-id {
            font-size: 1.4rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 1.2rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .order-id-badge {
            background: #34495e;
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.6rem 1.2rem;
            border-radius: 25px;
            color: white;
            font-weight: 600;
            margin: 1rem 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            animation: fadeIn 0.5s ease-in;
        }
        
        .status-placed {
            background: linear-gradient(135deg, #f1c40f, #f39c12);
        }
        
        .status-preparing {
            background: linear-gradient(135deg, #e67e22, #d35400);
        }
        
        .status-prepared {
            background: linear-gradient(135deg, #2ecc71, #27ae60);
        }
        
        .status-message {
            margin-top: 1.2rem;
            padding: 1.2rem;
            border-radius: 10px;
            background: #f8f9fa;
            font-size: 1.1rem;
            line-height: 1.5;
            border-left: 4px solid #3498db;
        }
        
        .status-timeline {
            display: flex;
            justify-content: space-between;
            margin: 2rem 0 1rem;
            position: relative;
        }
        
        .status-timeline::before {
            content: '';
            position: absolute;
            top: 15px;
            left: 0;
            width: 100%;
            height: 4px;
            background: #ecf0f1;
            z-index: 1;
        }
        
        .timeline-step {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 33.333%;
        }
        
        .step-icon {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background: #ecf0f1;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.5rem;
            color: #7f8c8d;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .step-text {
            font-size: 0.9rem;
            color: #7f8c8d;
            text-align: center;
            font-weight: 500;
        }
        
        .step-active .step-icon {
            background: #3498db;
            color: white;
            box-shadow: 0 0 0 5px rgba(52, 152, 219, 0.2);
        }
        
        .step-active .step-text {
            color: #2c3e50;
            font-weight: 600;
        }
        
        .step-completed .step-icon {
            background: #2ecc71;
            color: white;
        }
        
        .step-completed .step-text {
            color: #2ecc71;
        }
        </style>
    """, unsafe_allow_html=True)
    
    status_icons = {
        'placed': '🎯',
        'preparing': '👨‍🍳',
        'prepared': '✅'
    }
    
    status_messages = {
        'placed': 'Your order has been received and will be prepared soon. Please wait while we process your order.',
        'preparing': 'Our chefs are currently preparing your delicious meal. It won\'t be long before your food is ready!',
        'prepared': 'Great news! Your order is ready for pickup. Please collect it from the counter and enjoy your meal!'
    }
    
    status_class = f"status-{status}"
    icon = status_icons.get(status, '🔄')
    message = status_messages.get(status, 'Status information not available')
    
    # Determine which steps are active/completed based on current status
    timeline_states = {
        'placed': {'placed': 'active', 'preparing': '', 'prepared': ''},
        'preparing': {'placed': 'completed', 'preparing': 'active', 'prepared': ''},
        'prepared': {'placed': 'completed', 'preparing': 'completed', 'prepared': 'active'}
    }
    
    current_timeline = timeline_states.get(status, {'placed': '', 'preparing': '', 'prepared': ''})
    
    st.markdown(f"""
        <div class="order-status-container fade-in">
            <div class="order-id">
                Order <span class="order-id-badge">#{order_id}</span>
            </div>
            
            <div class="status-timeline">
                <div class="timeline-step step-{current_timeline['placed']}">
                    <div class="step-icon">1</div>
                    <div class="step-text">Placed</div>
                </div>
                <div class="timeline-step step-{current_timeline['preparing']}">
                    <div class="step-icon">2</div>
                    <div class="step-text">Preparing</div>
                </div>
                <div class="timeline-step step-{current_timeline['prepared']}">
                    <div class="step-icon">3</div>
                    <div class="step-text">Ready</div>
                </div>
            </div>
            
            <div class="status-badge {status_class}">
                {icon} {status.title()}
            </div>
            
            <div class="status-message">
                {message}
            </div>
        </div>
    """, unsafe_allow_html=True)

def display_order_history(orders):
    """Display order history with enhanced visual design and interactions"""
    st.markdown("""
        <style>
        .history-container {
            margin: 1.5rem 0;
        }
        
        .history-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1.2rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border: 1px solid #eee;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .history-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .history-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.2rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid #eee;
        }
        
        .history-order-id {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2c3e50;
        }
        
        .history-timestamp {
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-top: 0.3rem;
        }
        
        .payment-badge {
            display: inline-block;
            padding: 0.4rem 0.9rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .payment-cod {
            background: #e8f5e9;
            color: #2e7d32;
        }
        
        .payment-razorpay {
            background: #e3f2fd;
            color: #1565c0;
        }
        
        .history-items {
            margin: 1.2rem 0;
            padding: 1rem;
            background: #f8f9fa;
            border-radius: 10px;
        }
        
        .history-item {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px dashed #e0e0e0;
        }
        
        .history-item:last-child {
            border-bottom: none;
        }
        
        .item-name {
            font-weight: 500;
            color: #2c3e50;
        }
        
        .item-quantity {
            color: #7f8c8d;
            margin-right: 0.5rem;
        }
        
        .item-price {
            font-weight: 600;
            color: #2ecc71;
        }
        
        .history-total {
            text-align: right;
            font-size: 1.2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-top: 1rem;
            padding-top: 0.8rem;
            border-top: 2px solid #eee;
        }
        
        .history-total-amount {
            color: #2ecc71;
            font-size: 1.3rem;
        }
        
        .history-empty {
            text-align: center;
            padding: 3.5rem 2rem;
            background: #f8f9fa;
            border-radius: 12px;
            color: #7f8c8d;
            border: 2px dashed #e0e0e0;
            margin: 2rem 0;
        }
        
        .history-empty-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            color: #bdc3c7;
        }
        
        .history-empty-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #34495e;
            margin-bottom: 0.8rem;
        }
        
        .history-card-accent {
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background: linear-gradient(to bottom, #3498db, #2980b9);
        }
        </style>
    """, unsafe_allow_html=True)
    
    if orders.empty:
        st.markdown("""
            <div class="history-empty fade-in">
                <div class="history-empty-icon">📜</div>
                <div class="history-empty-title">No Order History</div>
                <p>Your past orders will appear here once you start ordering.</p>
            </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown('<div class="history-container">', unsafe_allow_html=True)
    
    for _, order in orders.iterrows():
        items = pd.read_json(order['items'])
        timestamp = pd.to_datetime(order['timestamp']).strftime("%d %b %Y at %I:%M %p")
        
        # Determine payment badge class
        payment_class = "payment-razorpay" if order['payment_method'].lower() == 'razorpay' else "payment-cod"
        
        st.markdown(f"""
            <div class="history-card slide-in">
                <div class="history-card-accent"></div>
                <div class="history-header">
                    <div>
                        <div class="history-order-id">Order #{order['order_id']}</div>
                        <div class="history-timestamp">{timestamp}</div>
                    </div>
                    <div class="payment-badge {payment_class}">
                        {order['payment_method'].upper()}
                    </div>
                </div>
                
                <div class="history-items">
        """, unsafe_allow_html=True)
        
        # Display items
        for _, item in items.iterrows():
            item_total = item['price'] * item['quantity']
            st.markdown(f"""
                <div class="history-item">
                    <div>
                        <span class="item-quantity">{item['quantity']}×</span>
                        <span class="item-name">{item['name']}</span>
                    </div>
                    <div class="item-price">₹{item_total:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
                </div>
                <div class="history-total">
                    Total: <span class="history-total-amount">₹{order['total_amount']:.2f}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_analytics(analytics_data):
    """Display analytics dashboard with enhanced visualizations and metrics"""
    st.markdown("""
        <style>
        .analytics-container {
            margin: 1.5rem 0;
        }
        
        .analytics-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border: 1px solid #eee;
            transition: all 0.3s ease;
        }
        
        .analytics-card:hover {
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .analytics-header {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 1.2rem;
            padding-bottom: 0.8rem;
            border-bottom: 2px solid #3498db;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .metric-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1.5rem;
            background: linear-gradient(135deg, #3498db, #2980b9);
            border-radius: 10px;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
        }
        
        .metric-value {
            font-size: 3rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }
        
        .metric-label {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        .chart-container {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
        }
        
        .chart-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        .no-data {
            text-align: center;
            padding: 2rem;
            color: #7f8c8d;
            background: #f8f9fa;
            border-radius: 10px;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="analytics-container fade-in">', unsafe_allow_html=True)
    
    # Create a row with metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="metric-container">
                <div class="metric-label">Total Orders</div>
                <div class="metric-value">{analytics_data['total_orders']}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        # Calculate total revenue if available
        total_revenue = 0
        if 'total_revenue' in analytics_data:
            total_revenue = analytics_data['total_revenue']
        
        st.markdown(f"""
            <div class="metric-container" style="background: linear-gradient(135deg, #2ecc71, #27ae60);">
                <div class="metric-label">Total Revenue</div>
                <div class="metric-value">₹{total_revenue:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        # Calculate average order value
        avg_order = 0
        if analytics_data['total_orders'] > 0 and 'total_revenue' in analytics_data:
            avg_order = analytics_data['total_revenue'] / analytics_data['total_orders']
        
        st.markdown(f"""
            <div class="metric-container" style="background: linear-gradient(135deg, #f39c12, #e67e22);">
                <div class="metric-label">Avg. Order Value</div>
                <div class="metric-value">₹{avg_order:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Create a row with charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
        st.markdown('<div class="analytics-header">💳 Payment Methods</div>', unsafe_allow_html=True)
        
        payment_stats = analytics_data['payment_stats']
        if not payment_stats.empty:
            # Add custom colors to the chart
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.bar_chart(payment_stats.set_index('payment_method'))
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="no-data">No payment data available</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
        st.markdown('<div class="analytics-header">🍽️ Most Popular Items</div>', unsafe_allow_html=True)
        
        most_sold = analytics_data['most_sold']
        if not most_sold.empty:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.bar_chart(most_sold.set_index('items'))
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="no-data">No sales data available</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional analytics section
    st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
    st.markdown('<div class="analytics-header">📊 Order Trends</div>', unsafe_allow_html=True)
    
    # If we have order trend data, display it
    if 'order_trends' in analytics_data and not analytics_data['order_trends'].empty:
        st.line_chart(analytics_data['order_trends'])
    else:
        # Create placeholder for order trends
        st.markdown('<div class="no-data">Order trend data not available</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close analytics container

def display_notifications(notifications, mark_as_read_callback):
    """Display notifications with enhanced styling and organization"""
    st.markdown("""
        <style>
        .notifications-container {
            margin: 1.5rem 0;
        }
        
        .notification-card {
            background: white;
            border-radius: 10px;
            padding: 1.2rem;
            margin: 0.8rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            border: 1px solid #eee;
            position: relative;
            overflow: hidden;
        }
        
        .notification-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .notification-unread {
            border-left: 4px solid #3498db;
            background: #f8f9fa;
        }
        
        .notification-message {
            font-size: 1rem;
            color: #2c3e50;
            line-height: 1.5;
            margin-bottom: 0.8rem;
        }
        
        .notification-time {
            font-size: 0.85rem;
            color: #7f8c8d;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .notification-badge {
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #3498db;
            border-radius: 50%;
            margin-right: 0.5rem;
        }
        
        .notification-actions {
            margin-top: 0.8rem;
            display: flex;
            justify-content: flex-end;
        }
        
        .notification-empty {
            text-align: center;
            padding: 2.5rem 1.5rem;
            background: #f8f9fa;
            border-radius: 10px;
            color: #7f8c8d;
            border: 2px dashed #e0e0e0;
            margin: 1.5rem 0;
        }
        
        .notification-empty-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: #bdc3c7;
        }
        
        .notification-empty-text {
            font-size: 1.1rem;
            font-weight: 500;
            color: #34495e;
            margin-bottom: 0.5rem;
        }
        
        .notification-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #3498db;
        }
        
        .notification-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #2c3e50;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .notification-count {
            background: #3498db;
            color: white;
            border-radius: 20px;
            padding: 0.2rem 0.8rem;
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        .mark-read-btn {
            background: none;
            border: none;
            color: #3498db;
            cursor: pointer;
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            transition: all 0.3s ease;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.3rem;
        }
        
        .mark-read-btn:hover {
            background: #e3f2fd;
            transform: translateY(-2px);
        }
        
        .notification-type-order {
            border-left-color: #2ecc71;
        }
        
        .notification-type-alert {
            border-left-color: #e74c3c;
        }
        
        .notification-type-info {
            border-left-color: #f39c12;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Count unread notifications
    unread_count = len(notifications[~notifications['is_read']]) if not notifications.empty else 0
    
    # Start notifications container
    st.markdown(f"""
        <div class="notifications-container fade-in">
            <div class="notification-header">
                <div class="notification-title">
                    📫 Notifications
                    {f'<span class="notification-count">{unread_count} new</span>' if unread_count > 0 else ''}
                </div>
            </div>
    """, unsafe_allow_html=True)
    
    if notifications.empty:
        st.markdown("""
            <div class="notification-empty slide-in">
                <div class="notification-empty-icon">📭</div>
                <div class="notification-empty-text">No Notifications</div>
                <p>You're all caught up! New notifications will appear here.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Sort notifications: unread first, then by timestamp
        notifications = notifications.sort_values(['is_read', 'timestamp'], ascending=[True, False])
        
        for _, notif in notifications.iterrows():
            is_unread = not notif['is_read']
            
            # Determine notification type based on content
            notif_type = "notification-type-info"
            if "order" in notif['message'].lower():
                notif_type = "notification-type-order"
            elif "alert" in notif['message'].lower() or "warning" in notif['message'].lower():
                notif_type = "notification-type-alert"
            
            # Format timestamp
            timestamp = pd.to_datetime(notif['timestamp']).strftime("%b %d, %Y at %I:%M %p")
            
            card_class = f"notification-card {'notification-unread' if is_unread else ''} {notif_type} slide-in"
            
            st.markdown(f"""
                <div class="{card_class}">
                    {f'<span class="notification-badge"></span>' if is_unread else ''}
                    <div class="notification-message">{notif['message']}</div>
                    <div class="notification-time">
                        <span>🕒</span> {timestamp}
                    </div>
            """, unsafe_allow_html=True)
            
            # Add mark as read button for unread notifications
            if is_unread:
                # Use Streamlit component for interactivity
                if st.button("✓ Mark as Read", key=f"read_{notif['id']}"):
                    mark_as_read_callback(notif['id'])
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Close notifications container
    st.markdown("</div>", unsafe_allow_html=True)








