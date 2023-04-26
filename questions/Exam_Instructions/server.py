def grade(data):
    data["score"] = 1
    if data["submitted_answers"]["accept"] == "accept":
    	data["submitted_answers"]["text"] = "A-Accept"
    elif data["submitted_answers"]["accept"] == "acceptminor":
    	data["submitted_answers"]["text"] = "B-Accept w/ Minor Revisions"
    elif data["submitted_answers"]["accept"] == "acceptmajor":
    	data["submitted_answers"]["text"] = "C-Accept w/ Major Revisions"
    else:
    	data["submitted_answers"]["text"] = "D-Reject"