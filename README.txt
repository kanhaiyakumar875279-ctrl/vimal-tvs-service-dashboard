
Vimal TVS Agency – Exotel Service Auto Call System
=================================================

WHAT THIS DOES
- Reads service-due customers from Excel
- Automatically calls customers using Exotel IVR
- On pressing 1, connects to Service Advisor

FILES
- service_data.xlsx  -> Update daily
- vimal_tvs_exotel_service.py -> Run this
- requirements.txt  -> Install dependencies

SETUP (ONE TIME)
1) Create Exotel account & complete KYC
2) Get:
   - EXOTEL_SID
   - API_KEY
   - API_TOKEN
   - EXOPHONE (virtual number)
3) Create IVR in Exotel Dashboard and copy IVR_ID
4) Edit vimal_tvs_exotel_service.py and paste credentials

RUN (DAILY)
pip install -r requirements.txt
python vimal_tvs_exotel_service.py

IMPORTANT
- Call only between 10 AM – 7 PM
- Do not call DND numbers
- Keep customer consent
