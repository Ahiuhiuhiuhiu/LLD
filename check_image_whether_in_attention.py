start = 0
gap = 500
for idx,i in enumerate(count[start:start+gap]):
    record = dataset_cam1.get_record(i)
    #if record.get_id() in tmp:
        #print('Pass')
        #continue
    print(start+idx,record.get_id())
    if record.get_id() not in Attention:
        #print("$$$$$$Attention$$$$$$")
        continue
    image_bytes = record.get_png()
    image_stream = io.BytesIO(image_bytes)
    image = np.array(Image.open(image_stream))
    plt.grid(b=False)
    plt.imshow(image)
    plt.show()
    #break