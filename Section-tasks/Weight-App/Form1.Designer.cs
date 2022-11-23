namespace Weight_App
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.masstxt = new System.Windows.Forms.TextBox();
            this.weightval_lbl = new System.Windows.Forms.Label();
            this.weighthl = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.Masslbl = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // masstxt
            // 
            this.masstxt.Location = new System.Drawing.Point(286, 159);
            this.masstxt.Name = "masstxt";
            this.masstxt.Size = new System.Drawing.Size(270, 23);
            this.masstxt.TabIndex = 0;
            this.masstxt.TextChanged += new System.EventHandler(this.masstxt_TextChanged);
            // 
            // weightval_lbl
            // 
            this.weightval_lbl.AutoSize = true;
            this.weightval_lbl.Location = new System.Drawing.Point(425, 202);
            this.weightval_lbl.Name = "weightval_lbl";
            this.weightval_lbl.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.weightval_lbl.Size = new System.Drawing.Size(39, 15);
            this.weightval_lbl.TabIndex = 1;
            this.weightval_lbl.Text = "Result";
            // 
            // weighthl
            // 
            this.weighthl.AutoSize = true;
            this.weighthl.Location = new System.Drawing.Point(365, 243);
            this.weighthl.Name = "weighthl";
            this.weighthl.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.weighthl.Size = new System.Drawing.Size(116, 15);
            this.weighthl.TabIndex = 2;
            this.weighthl.Text = "Too High or Too Low";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(374, 202);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(45, 15);
            this.label1.TabIndex = 3;
            this.label1.Text = "Weight";
            // 
            // Masslbl
            // 
            this.Masslbl.AutoSize = true;
            this.Masslbl.Location = new System.Drawing.Point(405, 127);
            this.Masslbl.Name = "Masslbl";
            this.Masslbl.Size = new System.Drawing.Size(34, 15);
            this.Masslbl.TabIndex = 4;
            this.Masslbl.Text = "Mass";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Masslbl);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.weighthl);
            this.Controls.Add(this.weightval_lbl);
            this.Controls.Add(this.masstxt);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private TextBox masstxt;
        private Label weightval_lbl;
        private Label weighthl;
        private Label label1;
        private Label Masslbl;
    }
}