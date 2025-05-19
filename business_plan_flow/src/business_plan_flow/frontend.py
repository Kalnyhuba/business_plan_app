import streamlit as st
import requests

st.set_page_config(page_title="Business Plan Creator", page_icon="📊")

# Initialize all required session state variables at the start
if 'page' not in st.session_state:
    st.session_state.page = 1
# Initialize session state for form fields if not exists
if 'business_name' not in st.session_state:
    st.session_state.business_name = ""
if 'start_year' not in st.session_state:
    st.session_state.start_year = ""
if 'business_reason' not in st.session_state:
    st.session_state.business_reason = ""
if 'mission_vision' not in st.session_state:
    st.session_state.mission_vision = ""
if 'legal_structure' not in st.session_state:
    st.session_state.legal_structure = None
if 'financial_funding' not in st.session_state:
    st.session_state.financial_funding = []
if 'business_sector' not in st.session_state:
    st.session_state.business_sector = None
if 'raw_materials_type' not in st.session_state:
    st.session_state.raw_materials_type = None
if 'industrial_business_type' not in st.session_state:
    st.session_state.industrial_business_type = None
if 'services_type' not in st.session_state:
    st.session_state.services_type = None
if 'durable_goods_type' not in st.session_state:
    st.session_state.durable_goods_type = None
if 'consumer_goods_type' not in st.session_state:
    st.session_state.consumer_goods_type = None
if 'healthcare_type' not in st.session_state:
    st.session_state.healthcare_type = None
if 'financial_sector_type' not in st.session_state:
    st.session_state.financial_sector_type = None
if 'it_sector_type' not in st.session_state:
    st.session_state.it_sector_type = None
if 'utilities_type' not in st.session_state:
    st.session_state.utilities_type = None
if 'culture_type' not in st.session_state:
    st.session_state.culture_type = None
if 'primary_countries' not in st.session_state:
    st.session_state.primary_countries = ""
if 'product_centralisation' not in st.session_state:
    st.session_state.product_centralisation = None
if 'characteristics' not in st.session_state:
    st.session_state.characteristics = []
if 'product_range' not in st.session_state:
    st.session_state.product_range = None
if 'end_consumer_characteristics' not in st.session_state:
    st.session_state.end_consumer_characteristics = None
if 'end_consumer_characteristics_2' not in st.session_state:
    st.session_state.end_consumer_characteristics_2 = []
if 'product_service_description' not in st.session_state:
    st.session_state.product_service_description = ""
# Page 2 session state initialization
if 'segment_name' not in st.session_state:
    st.session_state.segment_name = ""
if 'segment_demographics' not in st.session_state:
    st.session_state.segment_demographics = ""
if 'segment_characteristics' not in st.session_state:
    st.session_state.segment_characteristics = ""
if 'product_service_description' not in st.session_state:
    st.session_state.product_service_description = ""
if 'customer_count' not in st.session_state:
    st.session_state.customer_count = ""
if 'problems_faced' not in st.session_state:
    st.session_state.problems_faced = ""
if 'biggest_competitors' not in st.session_state:
    st.session_state.biggest_competitors = ""
if 'competition_intensity' not in st.session_state:
    st.session_state.competition_intensity = None
if 'price_comparison' not in st.session_state:
    st.session_state.price_comparison = None
if 'market_type' not in st.session_state:
    st.session_state.market_type = None
if 'competitive_parameters' not in st.session_state:
    st.session_state.competitive_parameters = []
if 'value_propositions' not in st.session_state:
    st.session_state.value_propositions = []
if 'direct_income' not in st.session_state:
    st.session_state.direct_income = None
if 'primary_revenue' not in st.session_state:
    st.session_state.primary_revenue = []
if 'one_time_payments' not in st.session_state:
    st.session_state.one_time_payments = []
if 'ongoing_payments' not in st.session_state:
    st.session_state.ongoing_payments = []
if 'payment_characteristics' not in st.session_state:
    st.session_state.payment_characteristics = []
if 'package_price' not in st.session_state:
    st.session_state.package_price = None
if 'price_negotiation' not in st.session_state:
    st.session_state.price_negotiation = None
if 'fixed_prices' not in st.session_state:
    st.session_state.fixed_prices = []
if 'dynamic_prices' not in st.session_state:
    st.session_state.dynamic_prices = []
if 'distribution_channels' not in st.session_state:
    st.session_state.distribution_channels = []
if 'purchasing_power' not in st.session_state:
    st.session_state.purchasing_power = None
if 'product_related_characteristics' not in st.session_state:
    st.session_state.product_related_characteristics = []
if 'self_service_availability' not in st.session_state:
    st.session_state.self_service_availability = None
if 'online_communities_presence' not in st.session_state:
    st.session_state.online_communities_presence = None
if 'development_process_customer_involvement' not in st.session_state:
    st.session_state.development_process_customer_involvement = None
if 'after_sale_purchases' not in st.session_state:
    st.session_state.after_sale_purchases = None
if 'personal_assistance_offered' not in st.session_state:
    st.session_state.personal_assistance_offered = None
if 'similar_products_switch' not in st.session_state:
    st.session_state.similar_products_switch = None
if 'general_customer_relation' not in st.session_state:
    st.session_state.general_customer_relation = None

st.title("Business Plan Creator")

col1, col2 = st.columns(2)
with col1:
    if st.session_state.page > 1:  # Only show Previous button if not on first page
        if st.button("Previous Page"):
            st.session_state.page -= 1
            st.rerun()
with col2:
    if st.session_state.page < 3:  # Only show Next button if not on last page
        if st.button("Next Page"):
            st.session_state.page += 1
            st.rerun()

if st.session_state.page == 1:
    st.header("Part 1: Basic information and market information")
    st.write("Initially we would like to ask some basic information about the company.")
    # Text input questions
    st.session_state.business_name = st.text_input(
        "What is the name of your company?",
        placeholder="e.g., EcoFashion",
        value=st.session_state.business_name
    )
    
    st.session_state.start_year = st.text_input(
        "In what year was your company established?",
        value=st.session_state.start_year
    )

    st.session_state.business_reason = st.text_area(
        "Kindly describe in maximum 500 characters why was your company established!",
        placeholder="e.g., In order to provide IT security services for small firms...",
        value=st.session_state.business_reason
    )

    st.session_state.mission_vision = st.text_area(
        "Please state your company's long-term goal or vision!",
        placeholder="e.g., Our mission is to...",
        value=st.session_state.mission_vision
    )

    # Single choice question
    st.session_state.legal_structure = st.radio(
        "What type of business is your company?",
        options=[
            "Sole proprietorship",
            "Private limited company",
            "General partnership",
            "Limited partnership",
            "Public limited company",
            "Association",
            "Branch of another company",
            "Non-profit"
        ],
        index=None if st.session_state.legal_structure is None else [
            "Sole proprietorship",
            "Private limited company",
            "General partnership",
            "Limited partnership",
            "Public limited company",
            "Association",
            "Branch of another company",
            "Non-profit"
        ].index(st.session_state.legal_structure)
    )

    st.session_state.financial_funding = st.multiselect(
        "How is your company currently financed?",
        options=[
            "Own financing",
            "Funding from investors",
            "Bank loan",
            "Revenue from sales",
            "Other"
        ],
        default=st.session_state.financial_funding,
        max_selections=5
    )

    st.session_state.business_sector = st.radio(
        "Which industrial sector does your company operate in?",
        options=[
            "Raw materials (eg mining, steel, trading companies)",
            "Industrial business (e.g. means of production, transport)",
            "Services (e.g. commercial and professional services, tourism)",
            "Durable consumer goods (e.g., furniture, clothing, retail)",
            "Fast-moving consumer goods (e.g., food, beverages, personal products)",
            "Healthcare (e.g., healthcare equipment, pharmaceuticals)",
            "Financial sectors (e.g., banks, insurance)",
            "Information technology",
            "Utilities and energy (e.g., water, heat, recycling)",
            "Culture and leisure (e.g., cultural centre, cinema)"
        ],
        index=None if st.session_state.business_sector is None else [
            "Raw materials (eg mining, steel, trading companies)",
            "Industrial business (e.g. means of production, transport)",
            "Services (e.g. commercial and professional services, tourism)",
            "Durable consumer goods (e.g., furniture, clothing, retail)",
            "Fast-moving consumer goods (e.g., food, beverages, personal products)",
            "Healthcare (e.g., healthcare equipment, pharmaceuticals)",
            "Financial sectors (e.g., banks, insurance)",
            "Information technology",
            "Utilities and energy (e.g., water, heat, recycling)",
            "Culture and leisure (e.g., cultural centre, cinema)"
        ].index(st.session_state.business_sector)
    )

    # Initialize sector-specific variables
    raw_materials_type = None
    industrial_business_type = None
    services_type = None
    durable_goods_type = None
    consumer_goods_type = None
    healtcare_type = None
    financial_sector_type = None
    it_sector_type = None
    utilities_type = None
    culture_type = None
    other_sector_type = None

    # Show sector-specific questions based on selection
    if st.session_state.business_sector == "Raw materials (eg mining, steel, trading companies)":
        st.session_state.raw_materials_type = st.radio(
            "What type of raw materials business is your company?",
            options=[
                "Mining",
                "Steel",
                "Trading companies",
                "Other"
            ],
            index=None if st.session_state.raw_materials_type is None else [
                "Mining",
                "Steel",
                "Trading companies",
                "Other"
            ].index(st.session_state.raw_materials_type)
        )
    elif st.session_state.business_sector == "Industrial business (e.g. means of production, transport)":
        st.session_state.industrial_business_type = st.radio(
            "What type of industrial business is your company?",
            options=[
                "Means of production",
                "Transport",
                "Other"
            ],
            index=None if st.session_state.industrial_business_type is None else [
                "Means of production",
                "Transport",
                "Other"
            ].index(st.session_state.industrial_business_type)
        )
    elif st.session_state.business_sector == "Services (e.g. commercial and professional services, tourism)":
        st.session_state.services_type = st.radio(
            "What type of services does your company provide?",
            options=[
                "Commercial services",
                "Professional services",
                "Tourism",
                "Other"
            ],
            index=None if st.session_state.services_type is None else [
                "Commercial services",
                "Professional services",
                "Tourism",
                "Other"
            ].index(st.session_state.services_type)
        )
    elif st.session_state.business_sector == "Durable consumer goods (e.g., furniture, clothing, retail)":
        st.session_state.durable_goods_type = st.radio(
            "What type of durable consumer goods does your company deal with?",
            options=[
                "Furniture",
                "Clothing",
                "Retail",
                "Other"
            ],
            index=None if st.session_state.durable_goods_type is None else [
                "Furniture",
                "Clothing",
                "Retail",
                "Other"
            ].index(st.session_state.durable_goods_type)
        )
    elif st.session_state.business_sector == "Fast-moving consumer goods (e.g., food, beverages, personal products)":
        st.session_state.consumer_goods_type = st.radio(
            "What type of consumer goods does your company deal with?",
            options=[
                "Food",
                "Beverages",
                "Personal products",
                "Other"
            ],
            index=None if st.session_state.consumer_goods_type is None else [
                "Food",
                "Beverages",
                "Personal products",
                "Other"
            ].index(st.session_state.consumer_goods_type)
        )
    elif st.session_state.business_sector == "Healthcare (e.g., healthcare equipment, pharmaceuticals)":
        st.session_state.healthcare_type = st.radio(
            "What type of healthcare business is your company?",
            options=[
                "Healthcare equipment",
                "Pharmaceuticals",
                "Other"
            ],
            index=None if st.session_state.healthcare_type is None else [
                "Healthcare equipment",
                "Pharmaceuticals",
                "Other"
            ].index(st.session_state.healthcare_type)
        )
    elif st.session_state.business_sector == "Financial sectors (e.g., banks, insurance)":
        st.session_state.financial_sector_type = st.radio(
            "What type of financial business is your company?",
            options=[
                "Banking",
                "Insurance",
                "Other"
            ],
            index=None if st.session_state.financial_sector_type is None else [
                "Banking",
                "Insurance",
                "Other"
            ].index(st.session_state.financial_sector_type)
        )
    elif st.session_state.business_sector == "Information technology":
        st.session_state.it_sector_type = st.radio(
            "What type of IT business is your company?",
            options=[
                "Software development",
                "Hardware",
                "IT services",
                "Other"
            ],
            index=None if st.session_state.it_sector_type is None else [
                "Software development",
                "Hardware",
                "IT services",
                "Other"
            ].index(st.session_state.it_sector_type)
        )
    elif st.session_state.business_sector == "Utilities and energy (e.g., water, heat, recycling)":
        st.session_state.utilities_type = st.radio(
            "What type of utilities business is your company?",
            options=[
                "Water",
                "Heat",
                "Recycling",
                "Other"
            ],
            index=None if st.session_state.utilities_type is None else [
                "Water",
                "Heat",
                "Recycling",
                "Other"
            ].index(st.session_state.utilities_type)
        )
    elif st.session_state.business_sector == "Culture and leisure (e.g., cultural centre, cinema)":
        st.session_state.culture_type = st.radio(
            "What type of culture and leisure business is your company?",
            options=[
                "Cultural centre",
                "Cinema",
                "Other"
            ],
            index=None if st.session_state.culture_type is None else [
                "Cultural centre",
                "Cinema",
                "Other"
            ].index(st.session_state.culture_type)
        )

    # Add missing questions
    st.session_state.primary_countries = st.text_area(
        "Please specify which country your company's primary market will be in the short-term (1-2 years). You can write multiple countries.",
        value=st.session_state.primary_countries if hasattr(st.session_state, 'primary_countries') else ""
    )

    st.session_state.characteristics = st.multiselect(
        "Please mark if one or more of the following statements characterize your company:",
        options=[
            "The company performs one or more specific function(s) in another company's value chain (e.g., logistics, waste management, cleaning service)",
            "New markets are continuously explored in order to obtain temporary monopolies",
            "Products developed for developing countries are repackaged and sold in developed countries",
            "Own developed R&D or knowledge is sold",
            "The company facilitates a platform for trading between buyers and sellers",
            "The company facilitates a platform for collaboration/marketing",
            "Other companies develop innovative products/services which are offered on the company's technological platform",
            "Tasks/products are regularly put up for tender for a bidding war between suppliers in order to reduce pruchase prices",
            "A small proportion of customers pay for the product/service, while a large proportion use it for free",
            "A large proportion of customers pay for the product/service, while a small proportion use it for free"
        ],
        default=st.session_state.characteristics if hasattr(st.session_state, 'characteristics') else []
    )

    st.session_state.product_centralisation = st.radio(
        "Is product/service development centralized or decentralized?",
        options=[
            "Centralized",
            "Decentralized"
        ],
        index=None if st.session_state.product_centralisation is None else [
            "Centralized",
            "Decentralized"
        ].index(st.session_state.product_centralisation)
    )

    st.session_state.product_range = st.radio(
        "Please specify what characterizes the product range of your company:",
        options=[
            "Single product category",
            "Multiple related product categories (such as office furniture and office supplies)",
            "Multiple unrelated product categories (e.g. TV's and vacuum cleaners)"
        ],
        index=None if st.session_state.product_range is None else [
            "Single product category",
            "Multiple related product categories (such as office furniture and office supplies)",
            "Multiple unrelated product categories (e.g. TV's and vacuum cleaners)"
        ].index(st.session_state.product_range)
    )

    st.session_state.end_consumer_characteristics = st.radio(
        "Please specify what characterizes the groups of end-consumers:",
        options=[
            "One specific customer group",
            "Several specific customer groups",
            "Several unspecific customer groups"
        ],
        index=None if st.session_state.end_consumer_characteristics is None else [
            "One specific customer group",
            "Several specific customer groups",
            "Several unspecific customer groups"
        ].index(st.session_state.end_consumer_characteristics)
    )

    st.session_state.end_consumer_characteristics_2 = st.multiselect(
        "Please specify what characterizes the groups of end-consumers:",
        options=[
            "End-consumers are primarily private individuals",
            "End-consumers are primarily companies",
            "End-consumers are primarily public institutions",
            "End-consumers are primarily non-profit organizations"
        ],
        default=st.session_state.end_consumer_characteristics_2
    )

    st.session_state.product_service_description = st.text_area(
            "Please write maximum 500 characters about the products or services that the company offers to customers.",
            placeholder="e.g., The company provides security services and advice to non-IT firms....",
            value=st.session_state.product_service_description
        )
    
    if st.button("Continue to Next Section"):
            st.session_state.page = 2
            st.rerun()

if st.session_state.page == 2:
    st.header("Part 2: Segmentation")
    st.write("In this section we would like to gather information about the products/services the company offers and about your most relevant customer segment.")
    st.write("Please provide information about your most relevant customer segment.")

    st.session_state.segment_name = st.text_input(
        "Name of your most relevant customer segment:",
        value=st.session_state.segment_name
    )

    st.session_state.segment_demographics = st.text_area(
        "Demographics of this customer segment (e.g., age, location, income level):",
        value=st.session_state.segment_demographics
    )

    st.session_state.segment_characteristics = st.text_area(
        "Characteristics of this customer segment (e.g., needs, preferences, behaviors):",
        value=st.session_state.segment_characteristics
    )

    st.session_state.customer_count = st.text_input(
        "How many customers does this segment have?",
        value=st.session_state.customer_count
    )

    st.session_state.problems_faced = st.text_area(
        "Please briefly describe the problems or challenges that your company is trying to solve for the customer group:",
        value=st.session_state.problems_faced
    )

    st.session_state.biggest_competitors = st.text_area(
        "Please indicate and name the three biggest competitors in relation to your company's sales to this customer group:",
        value=st.session_state.biggest_competitors
    )

    st.session_state.competition_intensity = st.radio(
        "Please indicate the intensity of the competition in the market:",
        options=[
            "Low",
            "Medium",
            "High"
        ],
        index=None if not st.session_state.competition_intensity else [
            "Low",
            "Medium",
            "High"
        ].index(st.session_state.competition_intensity)
    )

    st.session_state.price_comparison = st.radio(
        "How are the prices of your company's products/services compared to that of the competitors?",
        options=[
            "Significantly lower",
            "Similar",
            "Significantly higher"
        ],
        index=None if not st.session_state.price_comparison else [
            "Significantly lower",
            "Similar",
            "Significantly higher"
        ].index(st.session_state.price_comparison)
    )

    st.session_state.market_type = st.radio(
        "Is the market best described as a niche market or a mass market?",
        options=[
            "Niche market",
            "Mass market"
        ],
        index=None if not st.session_state.market_type else [
            "Niche market",
            "Mass market"
        ].index(st.session_state.market_type)
    )

    st.session_state.competitive_parameters = st.multiselect(
        "Now we compare your company with the competitors. Which competitve parameters does your company excel at towards the customer group? Select all that apply.",
        options=[
            "Best visual/aestethic design",
            "Convenience for customer",
            "Customized solutions",
            "Fast execution (from order to delivery)",
            "Fun/entertainment",
            "High brand value",
            "Long product/service life",
            "Free basic product/service",
            "Low price",
            "New/innovative",
            "Provides a wide range of products/services",
            "Quick introductions of new products/services",
            "Unique/limited available products and services",
            "Reduce customer's costs",
            "Reduce customer's risks",
            "Reliability and trust",
            "Product availability (the product/service is easy to acquire regardless of geographical location)",
            "Ease of use (the product/service is easy to use regardless of the company's help)",
            "Great sensory experience",
            "Knowledge/know-how",
            "Sustainable product(s)"
        ],
        default=st.session_state.competitive_parameters
    )

    st.session_state.value_propositions = st.multiselect(
        "Please select the most important value propositions towards the private end-consumers (Maximum of 5)",
        options=[
            "Social self-aggrandizement",
            "Brings hope",
            "Self-realization",
            "Motivation",
            "Inheritable",
            "Affiliation",
            "Reliability and trust",
            "Rewarding",
            "Nostalgia",
            "Attractive design",
            "Brand value",
            "Wellbeing",
            "Therapeutic value",
            "Entertainment",
            "Attractiveness",
            "Accessing",
            "Time saving",
            "Informs",
            "Appeals to the senses",
            "Wide selection",
            "Quality",
            "Avoids difficulties/hassles",
            "Connects",
            "Integrates",
            "Organizes",
            "Simplifies",
            "Risk reduction",
            "Membership benefits (e.g. discounts)",
            "Reduces costs/returns for the customer",
            "Reduces effort"
        ],
        default=st.session_state.value_propositions
    )

    st.session_state.direct_income = st.radio(
        "Does your company receive income directly from this customer group?",
        options=[
            "Yes",
            "No"
        ],
        index=None if not st.session_state.direct_income else [
            "Yes",
            "No"
        ].index(st.session_state.direct_income)
    )

    st.session_state.primary_revenue = st.multiselect(
        "How can your company's primary revenue from this customer group be characterized? Select all that apply.",
        options=[
            "One-time payments",
            "Partial payments (payment is split into several smaller parts, e.g. installments)",
            "Ongoing payments (e.g. subscriptions, licenses etc.)",
            "Barter (no money involved)",
            "Prepayments"
        ],
        default=st.session_state.primary_revenue
    )

    if "One-time payments" in st.session_state.primary_revenue:
        st.session_state.one_time_payments = st.multiselect(
            "Please specify which of the following one-time payments the revenue from this customer group primarily consists of: (Select 1 or more)",
            options=[
                "Cash payment (e.g., cash or invoice for ownership/consumption of product or service)",
                "Consumption settlement",
                "Leasing",
                "Licenses/royalties)",
                "Variable transaction fees (a percentage of the value of the transaction)",
                "Fixed transaction fees (fixed price)",
                "Voluntary contributions/sponsorships",
                "Sale of advertising space"
            ],
            default=st.session_state.one_time_payments
        )

    if st.session_state.primary_revenue and "Ongoing payments (e.g. subscriptions, licenses etc.)" in st.session_state.primary_revenue:
        st.session_state.ongoing_payments = st.multiselect(
            "Please specify which of the following ongoing payments the revenue from this customer group primarily consists of: (Select 1 or more)",
            options=[
                "Subscriptions",
                "Consumption settlement",
                "Leasing",
                "Licenses/royalties",
                "Variable transaction fees (a percentage of the value of the transaction)",
                "Fixed transaction fees (fixed price)",
                "Voluntary contributions/sponsorships",
                "Sale of advertising space"
            ],
            default=st.session_state.ongoing_payments
        )

    st.session_state.payment_characteristics = st.multiselect(
        "Select if any of the following statements characterize the primary income from this customer group:",
        options=[
            "Additional sales/sales of complementary products or services, with a high degree of coverage on the basis of the sale of a free or cheap product or service",
            "Sales of main product with high coverage to which complementary products are sold with a lower coverage",
            "Sales of continuous upgrades to the main product",
            "The company requires prepayments and achieves high profits due to low inventory cost",
            "The company collects products in package solution",
            "The customers are offed to purchase products together and share the ownership"
        ],
        default=st.session_state.payment_characteristics
    )

    st.session_state.package_price = st.radio(
        "What is the price on the package soultion compared to buying the individual products/services seperately?",
        options=[
            "Lower price",
            "Same price",
            "Higher price"
        ],
        index=None if not st.session_state.package_price else [
            "Lower price",
            "Same price",
            "Higher price"
        ].index(st.session_state.package_price)
    )

    st.session_state.price_negotiation = st.radio(
        "To what extent are the prices for the customers negotiable?",
        options=[
            "Fixed prices",
            "Dynamic/negotiable prices"
        ],
        index=None if not st.session_state.price_negotiation else [
            "Fixed prices",
            "Dynamic/negotiable prices"
        ].index(st.session_state.price_negotiation)
    )

    if st.session_state.price_negotiation == "Fixed prices":
        st.session_state.fixed_prices = st.multiselect(
            "Please specify what determines the fixed prices for the customers: (Select one or more)",
            options=[
                "The unit price is determined by the quantity purchased",
                "The unit price depends on the type and characteristics of the specific customer group",
                "The unit price is independent of quantity and the type and characteristics of the specific customer group",
                "The unit price is determined by varying use of the product",
                "The customer determines the price"
            ],
            default=st.session_state.fixed_prices
        )

    if st.session_state.price_negotiation == "Dynamic/negotiable prices":
        st.session_state.dynamic_prices = st.multiselect(
            "Please specify what determines the dynamic prices for the customers: (Select one or more)",
            options=[
                "The unit price is determined by the outcome of negotiation",
                "The unit price is determined by the outcome of bidding war",
                "The unit price is determined by varying use of the product",
                "The customer determines the price"
            ],
            default=st.session_state.dynamic_prices
        )

    st.session_state.distribution_channels = st.multiselect(
        "Which type of channels does the company use towards this customer group? (Select one or more)",
        options=[
            "Own physical location (e.g., shop or meeting room)",
            "Own webshop",
            "Own website",
            "Own outreach (e.g., own sales people or marketing channels)",
            "Retailers",
            "Wholesalers",
            "Independent private sales consultants",
            "Referrals from other companies",
            "Personal recommendation (word of mouth)"
            ],
            default=st.session_state.distribution_channels
        )

    st.session_state.purchasing_power = st.radio(
        "Please indicate this customer group's purchasing power:",
        options=[
            "Low purchasing power",
            "High purchasing power"
            ],
        index=None if not st.session_state.purchasing_power else [
            "Low purchasing power",
            "High purchasing power"
        ].index(st.session_state.purchasing_power)
        )

    st.session_state.product_related_characteristics = st.multiselect(
        "Please indicate if any of the following characteristics describes your company's products/services to this customer group compared with the competitors: (Select one or more)",
        options=[
            "A low number of different items (Limited selection)",
            "A high number of different items (Extensive selection)",
            "Large quantities of few items are sold",
            "Small quantities of many items are sold",
            "Low degree of coverage",
            "High degree of coverage"
            ],
            default=st.session_state.product_related_characteristics
        )

    st.session_state.self_service_availability = st.radio(
        "How often is this customer group offered self-service and automated processes (e.g., webshop or online banking)?",
        options=[
            "Never",
            "In some cases",
            "Always available"
        ],
        index=None if not st.session_state.self_service_availability else [
            "Never",
            "In some cases",
            "Always available"
        ].index(st.session_state.self_service_availability)
    )

    st.session_state.online_communities_presence = st.radio(
        "To what extent are online communites used to exchange information and solve the challenges of this customer group?",
        options=[
            "Never",
            "In some cases",
            "Always"
        ],
        index=None if not st.session_state.online_communities_presence else [
            "Never",
            "In some cases",
            "Always"
        ].index(st.session_state.online_communities_presence)
    )

    st.session_state.development_process_customer_involvement = st.radio(
        "To what extent is this customer group involved in the design or development process of products and services?",
        options=[
            "Never",
            "In some cases",
            "Always"
        ],
        index=None if not st.session_state.development_process_customer_involvement else [
            "Never",
            "In some cases",
            "Always"
        ].index(st.session_state.development_process_customer_involvement)
    )

    st.session_state.after_sale_purchases = st.radio(
        "How often does this customer group pay for after-sales services? (e.g., follow-up sale of service(s) or additional product(s). This does not mean resale)",
        options=[
            "Never",
            "In some cases",
            "Always"
        ],
        index=None if not st.session_state.after_sale_purchases else [
            "Never",
            "In some cases",
            "Always"
        ].index(st.session_state.after_sale_purchases)
    )

    st.session_state.personal_assistance_offered = st.radio(
        "What degree of personal assistance is offered?",
        options=[
            "None",
            "Somewhat (for example customer service department)",
            "High level of assistance (for example dedicated personal assistance manager)"
        ],
        index=None if not st.session_state.personal_assistance_offered else [
            "None",
            "Somewhat (for example customer service department)",
            "High level of assistance (for example dedicated personal assistance manager)"
        ].index(st.session_state.personal_assistance_offered)
    )

    st.session_state.similar_products_switch = st.radio(
        "How easy is it for customers to switch to other providers of similar products/services?",
        options=[
            "Impossible",
            "Only possible with significant effort or research",
            "Possible, but takes effort",
            "Easy, with a bit of effort",
            "Extremely easy"
        ],
        index=None if not st.session_state.similar_products_switch else [
            "Impossible",
            "Only possible with significant effort or research",
            "Possible, but takes effort",
            "Easy, with a bit of effort",
            "Extremely easy"
        ].index(st.session_state.similar_products_switch)
    )

    st.session_state.general_customer_relation = st.radio(
        "How is the relation with this customer group in general?",
        options=[
            "One-time purchase",
            "Occasional buyer",
            "Regular customer",
            "Frequent buyer",
            "Long-term relation"
        ],
        index=None if not st.session_state.general_customer_relation else [
            "One-time purchase",
            "Occasional buyer",
            "Regular customer",
            "Frequent buyer",
            "Long-term relation"
        ].index(st.session_state.general_customer_relation)
    )

    # Add continue button
    #if st.button("Continue to Next Section"):
    #    st.session_state.page = 3
    #    st.rerun()

if st.button("Generate Business Plan"):
    with st.spinner("🧠 Generating your business plan..."):
        try:
            data = {
                "business_name": st.session_state.business_name,
                    "start_year": st.session_state.start_year,
                    "business_reason": st.session_state.business_reason,
                    "mission_vision": st.session_state.mission_vision,
                    "legal_structure": st.session_state.legal_structure,
                    "financial_funding": st.session_state.financial_funding,
                    "business_sector": st.session_state.business_sector,
                    "raw_materials_type": st.session_state.raw_materials_type,
                    "industrial_business_type": st.session_state.industrial_business_type,
                    "services_type": st.session_state.services_type,
                    "durable_goods_type": st.session_state.durable_goods_type,
                    "consumer_goods_type": st.session_state.consumer_goods_type,
                    "healthcare_type": st.session_state.healthcare_type,
                    "financial_sector_type": st.session_state.financial_sector_type,
                    "it_sector_type": st.session_state.it_sector_type,
                    "utilities_type": st.session_state.utilities_type,
                    "culture_type": st.session_state.culture_type,
                    "primary_countries": st.session_state.primary_countries,
                    "product_centralisation": st.session_state.product_centralisation,
                    "product_range": st.session_state.product_range,
                    "end_consumer_characteristics": st.session_state.end_consumer_characteristics,
                    "end_consumer_characteristics_2": st.session_state.end_consumer_characteristics_2,
                    "product_service_description": st.session_state.product_service_description,
                    "segment_name": st.session_state.segment_name,
                    "segment_demographics": st.session_state.segment_demographics,
                    "segment_characteristics": st.session_state.segment_characteristics,
                    "customer_count": st.session_state.customer_count,
                    "problems_faced": st.session_state.problems_faced,
                    "biggest_competitors": st.session_state.biggest_competitors,
                    "competition_intensity": st.session_state.competition_intensity,
                    "price_comparison": st.session_state.price_comparison,
                    "market_type": st.session_state.market_type,
                    "competitive_parameters": st.session_state.competitive_parameters,
                    "value_propositions": st.session_state.value_propositions,
                    "direct_income": st.session_state.direct_income,
                    "primary_revenue": st.session_state.primary_revenue,
                    "one_time_payments": st.session_state.one_time_payments,
                    "ongoing_payments": st.session_state.ongoing_payments,
                    "payment_characteristics": st.session_state.payment_characteristics,
                    "package_price": st.session_state.package_price,
                    "price_negotiation": st.session_state.price_negotiation,
                    "fixed_prices": st.session_state.fixed_prices,
                    "dynamic_prices": st.session_state.dynamic_prices,
                    "distribution_channels": st.session_state.distribution_channels,
                    "purchasing_power": st.session_state.purchasing_power,
                    "product_related_characteristics": st.session_state.product_related_characteristics,
                    "self_service_availability": st.session_state.self_service_availability,
                    "online_communities_presence": st.session_state.online_communities_presence,
                    "development_process_customer_involvement": st.session_state.development_process_customer_involvement,
                    "after_sale_purchases": st.session_state.after_sale_purchases,
                    "personal_assistance_offered": st.session_state.personal_assistance_offered,
                    "similar_products_switch": st.session_state.similar_products_switch,
                    "general_customer_relation": st.session_state.general_customer_relation
            }

            st.write("🔄 Sending data for processing...")

            response = requests.post(
                "http://localhost:8000/generate_business_plan",
                json=data
            )

            if response.status_code == 200:
                result = response.json()
                business_plan_sections = result["business_plan"]

                # Display each section with progress bar
                progress = st.progress(0)
                full_content = "# Business Plan\n\n"
                num_sections = len(business_plan_sections)

                for i, section in enumerate(business_plan_sections):
                    st.markdown(section, unsafe_allow_html=True)
                    st.markdown("---")
                    full_content += section + "\n\n---\n\n"
                    progress.progress((i + 1) / num_sections)

                st.success("✅ Business Plan ready!")

                st.download_button(
                    label="Download Business Plan",
                    data=full_content,
                    file_name="generated_business_plan.md",
                    mime="text/markdown"
                )
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Error connecting to the server: {str(e)}")
                