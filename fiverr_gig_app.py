import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from PIL import Image, ImageTk
import os
from ttkthemes import ThemedTk

class FiverrGigApp(ThemedTk):
    def __init__(self):
        super().__init__()

        self.set_theme("plastik")  # Set a default theme (you can change this)

        self.title("Fiverr Gig Template")
        self.geometry("950x700")
        self.minsize(800, 600)

        self.template = {
            "gig_title": "I will design a stunning logo for your brand",
            "gig_category": "Graphics & Design",
            "gig_subcategory": "Logo Design",
            "service_type": "",
            "gig_metadata": "",
            "gig_description": """
            I am a professional logo designer with 5+ years of experience. I will create a unique and memorable logo that perfectly represents your brand.

            **What you can expect:**
            - Unique and creative logo concepts
            - Unlimited revisions until you are satisfied
            - High-resolution files (JPG, PNG, AI, EPS)
            - Fast turnaround time
            - Excellent customer service

            Let's build your brand together!
            """,
            "pricing_packages": {
                "basic": {
                    "title": "Basic Logo Package",
                    "description": "One basic logo concept, JPG/PNG files, 2 revisions",
                    "delivery_time": "3 days",
                    "price": 25,
                    "revisions": 2,
                    "features": ["1 Basic Concept", "JPG/PNG Files", "2 Revisions"]
                },
                "standard": {
                    "title": "Standard Logo Package",
                    "description": "Two logo concepts, source file, unlimited revisions, faster delivery",
                     "delivery_time": "2 days",
                     "price": 50,
                     "revisions": "Unlimited",
                    "features": ["2 Logo Concepts", "Source File", "Unlimited Revisions", "Faster Delivery"]
                },
                "premium": {
                    "title": "Premium Logo Package",
                    "description": "Three logo concepts, source file, brand style guide, premium support",
                     "delivery_time": "1 day",
                     "price": 100,
                     "revisions": "Unlimited",
                    "features": ["3 Logo Concepts", "Source File", "Brand Style Guide", "Priority Support"]
                }
            },
            "requirements": "Please provide me with your brand name, a brief description of your business, any color preferences, and any examples of logos you like.",
            "gallery": {
                "images": [],
                "videos": [],
                "audios": [],
                "pdfs": []
                },
             "faq": [
                {"question":"What is included in the source file?","answer":"The source file is an AI or EPS file that is editable and can be scaled without loss of quality"},
                {"question":"Do you offer revisions?","answer":"Yes, all packages include revisions, with the standard and premium offering unlimited"},
                {"question":"Can I use the logo commercially?","answer":"Yes, all packages include the full commercial rights to the logo"}
            ]
        }

        self.create_widgets()

    def create_widgets(self):
        # Main Notebook (Tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # Overview Tab
        self.overview_tab = self.create_tab(self.notebook, "Overview")
        self.create_overview_tab(self.overview_tab)

        # Pricing Tab
        self.pricing_tab = self.create_tab(self.notebook, "Pricing")
        self.create_pricing_tab(self.pricing_tab)

        # Description & FAQ Tab
        self.description_faq_tab = self.create_tab(self.notebook, "Description & FAQ")
        self.create_description_faq_tab(self.description_faq_tab)

        # Requirements Tab
        self.requirements_tab = self.create_tab(self.notebook, "Requirements")
        self.create_requirements_tab(self.requirements_tab)

        # Gallery Tab
        self.gallery_tab = self.create_tab(self.notebook, "Gallery")
        self.create_gallery_tab(self.gallery_tab)

    def create_tab(self, notebook, text):
      tab = ttk.Frame(notebook)
      notebook.add(tab, text=text)
      tab.rowconfigure(0, weight=1)
      tab.columnconfigure(0, weight=1)
      return tab

    def create_overview_tab(self, parent):
         # Padding for the entire tab
        parent.grid_propagate(False)
        for i in range(12):  # Add padding for first 12 rows in Overview
           parent.rowconfigure(i, weight=0)

        # Gig Title
        self.gig_title_entry = self.create_label_entry(parent, "Gig Title:", 0, 0, self.template["gig_title"], True, self.validate_gig_title, "Make sure your title is short, clear, and to the point. Buyers should immediately recognize the service you provide.")
        # Category
        self.category_entry = self.create_label_entry(parent, "Category:", 2, 0, self.template["gig_category"], False, None, "Select the correct Category. You won't be able to change this once published.")
         # Subcategory
        self.subcategory_entry = self.create_label_entry(parent, "Subcategory:", 4, 0, self.template["gig_subcategory"], False, None, "Select the correct Subcategory. You won't be able to change this once published.")
        # Service Type
        self.service_type_dropdown = self.create_dropdown(parent, "Service Type:", 6, 0, ["", "Logo Design", "Brand Style Guide", "Web Design", "Other"], self.template["service_type"], "Select the type of service you provide.")
        # Gig Metadata
        self.metadata_entry = self.create_label_entry(parent, "Gig Metadata:", 8, 0, self.template["gig_metadata"], False, None, "Select the relevant criteria for each topic. (Only available for certain categories).")
        # Search Tags
        self.search_tag_entry = self.create_label_entry(parent, "Search Tags:", 10, 0, "", False, None, "Add up to 5 words or phrases that best describe your Gig.")

    def create_label_entry(self, parent, label_text, row, col, initial_value, validate, validation_command, tooltip_text):
        ttk.Label(parent, text=label_text, font=("Arial", 10, "bold")).grid(row=row, column=col, sticky=tk.W, padx=5, pady=5)
        entry = ttk.Entry(parent, width=70)
        entry.insert(0, initial_value)
        entry.grid(row=row, column=col + 1, sticky=tk.EW, padx=5, pady=5)
        if validate:
          entry.bind("<FocusOut>", validation_command)
        ttk.Label(parent, text=tooltip_text, wraplength=500, justify="left", font=('Arial', 8, 'italic')).grid(row=row+1, column=col+1, sticky=tk.W, padx=5, pady=0)
        return entry

    def create_dropdown(self, parent, label_text, row, col, values, initial_value, tooltip_text):
        ttk.Label(parent, text=label_text, font=("Arial", 10, "bold")).grid(row=row, column=col, sticky=tk.W, padx=5, pady=5)
        var = tk.StringVar(value=initial_value)
        dropdown = ttk.Combobox(parent, textvariable=var, values=values, state='readonly', width=30)
        dropdown.grid(row=row, column=col + 1, sticky=tk.W, padx=5, pady=5)
        ttk.Label(parent, text=tooltip_text, wraplength=500, justify="left", font=('Arial', 8, 'italic')).grid(row=row+1, column=col+1, sticky=tk.W, padx=5, pady=0)
        return dropdown


    def create_pricing_tab(self, parent):
        parent.grid_propagate(False)
        for i in range(len(self.template["pricing_packages"]) * 7): # Add space for each pricing row.
            parent.rowconfigure(i, weight=0)


        for i, (package_name, package_details) in enumerate(self.template["pricing_packages"].items()):

            ttk.Label(parent, text=f'{package_details["title"]}:', font=('Arial', 12, 'bold')).grid(row=i*7, column=0, sticky=tk.W, padx=5, pady=5, columnspan=2)

             # Package Description
            ttk.Label(parent, text="Description:", font=("Arial", 10, "bold")).grid(row=i*7+1, column=0, sticky=tk.W, padx=5, pady=5)
            package_details["description_text"] = scrolledtext.ScrolledText(parent, wrap=tk.WORD, width=60, height=3)
            package_details["description_text"].insert(tk.END, package_details["description"])
            package_details["description_text"].grid(row=i*7+1, column=1, sticky="ew", padx=5, pady=5)

            # Delivery Time
            ttk.Label(parent, text="Delivery Time:", font=("Arial", 10, "bold")).grid(row=i*7+2, column=0, sticky=tk.W, padx=5, pady=5)
            package_details["delivery_time_entry"] = ttk.Entry(parent, width=10)
            package_details["delivery_time_entry"].insert(0, package_details["delivery_time"])
            package_details["delivery_time_entry"].grid(row=i*7+2, column=1, sticky=tk.W, padx=5, pady=5)
            package_details["delivery_time_entry"].bind("<FocusOut>", lambda event, pkg=package_details: self.validate_delivery_time(event, pkg))


             # Price
            ttk.Label(parent, text="Price:", font=("Arial", 10, "bold")).grid(row=i*7+3, column=0, sticky=tk.W, padx=5, pady=5)
            package_details["price_entry"] = ttk.Entry(parent, width=10)
            package_details["price_entry"].insert(0, package_details["price"])
            package_details["price_entry"].grid(row=i*7+3, column=1, sticky=tk.W, padx=5, pady=5)
            package_details["price_entry"].bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_price(event, pkg))

            # Revisions
            ttk.Label(parent, text="Revisions:", font=("Arial", 10, "bold")).grid(row=i*7+4, column=0, sticky=tk.W, padx=5, pady=5)
            package_details["revisions_entry"] = ttk.Entry(parent, width=10)
            package_details["revisions_entry"].insert(0, package_details["revisions"])
            package_details["revisions_entry"].grid(row=i*7+4, column=1, sticky=tk.W, padx=5, pady=5)
            package_details["revisions_entry"].bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_revisions(event, pkg))


            # Features
            ttk.Label(parent, text="Features:", font=("Arial", 10, "bold")).grid(row=i*7+5, column=0, sticky=tk.W, padx=5, pady=5)
            package_details["features_entry"] = ttk.Entry(parent, width=70)
            package_details["features_entry"].insert(0, ', '.join(package_details["features"]))
            package_details["features_entry"].grid(row=i*7+5, column=1, sticky=tk.EW, padx=5, pady=5)
            ttk.Label(parent, text="Note: Use comma separated values to add features.", wraplength=500, justify="left", font=('Arial', 8, 'italic')).grid(row=i*7+6, column=1, sticky=tk.W, padx=5, pady=0)


    def create_description_faq_tab(self, parent):
         # Add padding
        parent.grid_propagate(False)
        parent.rowconfigure(1, weight=1)
        parent.rowconfigure(4, weight=1)


         # Gig Description
        ttk.Label(parent, text="Gig Description:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.description_text = scrolledtext.ScrolledText(parent, wrap=tk.WORD, width=80, height=10)
        self.description_text.insert(tk.END, self.template["gig_description"])
        self.description_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        ttk.Label(parent, text="Briefly describe your Gig (up to 1,200 characters). Include only URLs from Fiverr's approved list.", wraplength=700, justify="left", font=('Arial', 8, 'italic')).grid(row=2, column=0, sticky=tk.W, padx=5, pady=0)

        # FAQ Section
        ttk.Label(parent, text="FAQ:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.faq_frame = ttk.Frame(parent)
        self.faq_frame.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
        self.faq_entries = []
        self.update_faq_entries()
        ttk.Label(parent, text="Add answers to the most commonly asked questions (limit of 10 FAQs).", wraplength=700, justify="left", font=('Arial', 8, 'italic')).grid(row=5, column=0, sticky=tk.W, padx=5, pady=0)

        add_faq_button = ttk.Button(parent, text="Add FAQ", command=self.add_faq)
        add_faq_button.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)


    def create_requirements_tab(self, parent):
         # Padding
        parent.grid_propagate(False)
        parent.rowconfigure(1, weight=1)

        ttk.Label(parent, text="Requirements:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.requirements_text = scrolledtext.ScrolledText(parent, wrap=tk.WORD, width=80, height=10)
        self.requirements_text.insert(tk.END, self.template["requirements"])
        self.requirements_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        ttk.Label(parent, text="Enter the details of your requirements from the buyer.", wraplength=700, justify="left", font=('Arial', 8, 'italic')).grid(row=2, column=0, sticky=tk.W, padx=5, pady=0)


    def create_gallery_tab(self, parent):
         # Add padding
        parent.grid_propagate(False)

         # Image Upload
        ttk.Label(parent, text="Images:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.NW, padx=5, pady=5)
        ttk.Label(parent, text="Recommended size: 1280x769 px (72 DPI), min: 712x430 px.", wraplength=600, justify="left", font=('Arial', 8, 'italic')).grid(row=1, column=1, sticky=tk.W, padx=5, pady=0)
        image_frame = ttk.Frame(parent)
        image_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.image_labels = []
        self.update_image_gallery(image_frame)

        upload_image_button = ttk.Button(parent, text="Upload Image", command=self.upload_image)
        upload_image_button.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        # Video Upload
        ttk.Label(parent, text="Videos:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(parent, text="Video should be 20-60 seconds, under 50 MB. Mention that your services are offered exclusively on Fiverr.", wraplength=600, justify="left", font=('Arial', 8, 'italic')).grid(row=5, column=1, sticky=tk.W, padx=5, pady=0)
        self.video_label = ttk.Label(parent, text="No video selected", wraplength=600, justify="left")
        self.video_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        upload_video_button = ttk.Button(parent, text="Upload Video", command=self.upload_video)
        upload_video_button.grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)

        # Audio Upload
        ttk.Label(parent, text="Audio:", font=("Arial", 10, "bold")).grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(parent, text="Supported formats: mp3 and MPEG. Make sure your audio isn't longer than 3:30 minutes, and less than 10MB.", wraplength=600, justify="left", font=('Arial', 8, 'italic')).grid(row=9, column=1, sticky=tk.W, padx=5, pady=0)
        self.audio_label = ttk.Label(parent, text="No audio selected")
        self.audio_label.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        upload_audio_button = ttk.Button(parent, text="Upload Audio", command=self.upload_audio)
        upload_audio_button.grid(row=11, column=0, sticky=tk.W, padx=5, pady=5)

        # PDF Upload
        ttk.Label(parent, text="PDF:", font=("Arial", 10, "bold")).grid(row=12, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(parent, text="You can upload up to 2 PDF files. Only the first 3 pages will be displayed.", wraplength=600, justify="left", font=('Arial', 8, 'italic')).grid(row=13, column=1, sticky=tk.W, padx=5, pady=0)
        self.pdf_label = ttk.Label(parent, text="No PDF selected")
        self.pdf_label.grid(row=14, column=0, sticky="w", padx=5, pady=5)
        upload_pdf_button = ttk.Button(parent, text="Upload PDF", command=self.upload_pdf)
        upload_pdf_button.grid(row=15, column=0, sticky=tk.W, padx=5, pady=5)


    def validate_gig_title(self, event):
         title = self.gig_title_entry.get()
         if not title:
            messagebox.showerror("Error", "Gig Title cannot be empty.")
            self.gig_title_entry.focus()

    def validate_delivery_time(self, event, package_details):
            entry = package_details["delivery_time_entry"]
            try:
                entry.unbind("<FocusOut>")
                delivery_time = int(entry.get())
                if delivery_time < 1:
                   messagebox.showerror("Error", f"Delivery time for {package_details['title']} must be 1 day or more.")
                   entry.delete(0, tk.END)
                   entry.focus()
                else:
                    entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_delivery_time(event, pkg))
            except ValueError:
                   messagebox.showerror("Error", f"Delivery time for {package_details['title']} must be a number.")
                   entry.delete(0, tk.END)
                   entry.focus()
            finally:
                  entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_delivery_time(event, pkg))

    def validate_price(self, event, package_details):
           entry = package_details["price_entry"]
           try:
                entry.unbind("<FocusOut>")
                price = int(entry.get())
                if price < 5:
                    messagebox.showerror("Error", f"Price for {package_details['title']} must be $5 or more.")
                    entry.delete(0, tk.END)
                    entry.focus()
                else:
                    entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_price(event, pkg))

           except ValueError:
                messagebox.showerror("Error", f"Price for {package_details['title']} must be a number.")
                entry.delete(0, tk.END)
                entry.focus()
           finally:
                 entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_price(event, pkg))


    def validate_revisions(self, event, package_details):
             entry = package_details["revisions_entry"]
             entry.unbind("<FocusOut>")
             revisions = entry.get()
             if revisions.lower() == "unlimited":
                entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_revisions(event, pkg))
                return
             try:
                revisions_int = int(revisions)
                if revisions_int < 0:
                   messagebox.showerror("Error", f"Number of revisions for {package_details['title']} must be 0 or more.")
                   entry.delete(0, tk.END)
                   entry.focus()
                else:
                    entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_revisions(event, pkg))
             except ValueError:
                  messagebox.showerror("Error", f"Revisions for {package_details['title']} must be a number or 'Unlimited'.")
                  entry.delete(0, tk.END)
                  entry.focus()
             finally:
                entry.bind("<FocusOut>",  lambda event, pkg=package_details: self.validate_revisions(event, pkg))


    def update_faq_entries(self):
      for widget in self.faq_frame.winfo_children():
          widget.destroy()

      for i, qa in enumerate(self.template["faq"]):
           ttk.Label(self.faq_frame, text=f"Q{i+1}:", font=("Arial", 10, "bold")).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
           question_entry = ttk.Entry(self.faq_frame, width=60)
           question_entry.insert(0, qa["question"])
           question_entry.grid(row=i, column=1, sticky=tk.EW, padx=5, pady=5)
           self.faq_entries.append(question_entry)

           ttk.Label(self.faq_frame, text="A:", font=("Arial", 10, "bold")).grid(row=i, column=2, sticky=tk.W, padx=5, pady=5)
           answer_entry = ttk.Entry(self.faq_frame, width=60)
           answer_entry.insert(0, qa["answer"])
           answer_entry.grid(row=i, column=3, sticky=tk.EW, padx=5, pady=5)
           self.faq_entries.append(answer_entry)

           remove_faq_button = ttk.Button(self.faq_frame, text="Remove", command=lambda idx=i: self.remove_faq(idx))
           remove_faq_button.grid(row=i, column=4, sticky=tk.W, padx=5, pady=5)
      if len(self.template["faq"]) >= 10:
          messagebox.showwarning("Warning", "Maximum limit of 10 FAQs reached.")


    def add_faq(self):
        if len(self.template["faq"]) < 10:
          self.template["faq"].append({"question": "", "answer": ""})
          self.update_faq_entries()
        else:
          messagebox.showwarning("Warning", "Maximum limit of 10 FAQs reached.")


    def remove_faq(self, index):
        del self.template["faq"][index]
        self.update_faq_entries()

    def update_image_gallery(self, frame):
       for widget in frame.winfo_children():
          widget.destroy()

       for i, image_path in enumerate(self.template["gallery"]["images"]):
            try:
                image = Image.open(image_path)
                image.thumbnail((100,100))
                photo = ImageTk.PhotoImage(image)
                label = ttk.Label(frame, image=photo)
                label.image = photo #keep a reference to the image
                label.grid(row=0, column=i, padx=5, pady=5)
                self.image_labels.append(label)

                remove_image_button = ttk.Button(frame, text="Remove", command=lambda idx=i: self.remove_image(idx))
                remove_image_button.grid(row=1, column=i, sticky=tk.W, padx=5, pady=5)

            except Exception as e:
                print(f"Error loading image: {e}")



    def remove_image(self, index):
         del self.template["gallery"]["images"][index]
         self.update_image_gallery(self.children['!frame3'])


    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.template["gallery"]["images"].append(file_path)
            self.update_image_gallery(self.children['!frame3'])



    def upload_video(self):
         file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mov *.avi")])
         if file_path:
             if len(self.template["gallery"]["videos"]) > 0:
                self.template["gallery"]["videos"] = [file_path]
             else:
                self.template["gallery"]["videos"].append(file_path)
             self.video_label.config(text=os.path.basename(file_path))



    def upload_audio(self):
       file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.mpeg")])
       if file_path:
            if len(self.template["gallery"]["audios"]) > 0:
                self.template["gallery"]["audios"] = [file_path]
            else:
                self.template["gallery"]["audios"].append(file_path)
            self.audio_label.config(text=os.path.basename(file_path))



    def upload_pdf(self):
       file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
       if file_path:
            if len(self.template["gallery"]["pdfs"]) > 1:
               messagebox.showwarning("Warning", "Maximum limit of 2 PDFs reached.")
            elif len(self.template["gallery"]["pdfs"]) > 0:
               self.template["gallery"]["pdfs"] = [file_path]
            else:
                self.template["gallery"]["pdfs"].append(file_path)
            self.pdf_label.config(text=os.path.basename(file_path))


if __name__ == "__main__":
    app = FiverrGigApp()
    app.mainloop()