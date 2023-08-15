def open_new_page():
    # Hide the current page's elements
    search_label.pack_forget()
    search_entry.pack_forget()
    search_button.pack_forget()
    results_text.pack_forget()
    follow_label.pack_forget()
    github_button.pack_forget()

    # Create a new frame for the new page
    new_page_frame = tk.Frame(root)
    new_page_frame.pack()

    # Add elements to the new page frame
    new_page_label = tk.Label(new_page_frame, text="This is a new page!")
    new_page_label.pack()

    # Add a button to go back to the file search page
    back_to_search_button = tk.Button(new_page_frame, text="Back to Search", command=back_to_search)
    back_to_search_button.pack()

def back_to_search():
    # Destroy the new page frame and show the file search page elements
    new_page_frame.destroy()
    search_label.pack()
    search_entry.pack()
    search_button.pack()
    results_text.pack()
    follow_label.pack(side=tk.BOTTOM)
    github_button.pack(side=tk.BOTTOM)
