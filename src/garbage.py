    def __load_embeddings(self, path : str) -> Tensor:
        OPEN = True
        if path not in os.listdir("."):
            os.mkdir(f"./{path}")
        dir = f"./{path}/{self.model.encoder_name()}"
        if self.model.encoder_name() not in os.listdir(f"./{path}"):
            os.mkdir(dir)
        corpus_hash = hash(self.corpus)
        file_path = f"./{dir}/{corpus_hash}"
        if OPEN and f"{corpus_hash}" in os.listdir(dir):
            files = os.listdir(file_path)
            files_lists = []
            batch_size = len(files) // THREADS
            i = 0
            for i in range(THREADS - 1, batch_size):
                files_lists.append(files[i : i + batch_size])
            files_lists.append(files[i:])
            threads : list[multiprocessing.Process] = []
            out_lists = []
            for fl in files_lists:
                encs = []
                threads.append(multiprocessing.Process(target=self.__load_file_list, args=(fl,encs)))
                out_lists.append(encs)
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            final_encs = []
            for encs in out_lists:
                final_encs.extend(encs)
            return self.__combine_embeddings(final_encs)
        else:
            os.mkdir(file_path)
            encs = []
            for i,text in enumerate(self.corpus.texts):
                enc = self.model(text)
                with open(file_path + f"/{i}", "wb") as f:
                    torch.save(enc, f) #replace with torch.load
                encs.append(enc)
            return self.__combine_embeddings(encs)


    def __load_file_list(self, path : str, files : list[str], out_tensors : list[Tensor]) -> None:
        for f in files:
            with open(path + f"/{f}", "rb") as f:
                enc = torch.load(f) 
                out_tensors.append(enc)